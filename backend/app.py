import sys
print(sys.executable)

from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import timedelta

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import hashlib

from dotenv import load_dotenv
import os



load_dotenv("sendgrid.env")  # This loads the .env file at the path given, or default to the .env file in the same directory as the script.

# Now you can safely access the environment variable
api_key = os.getenv('SENDGRID_API_KEY')
if api_key is None:
    raise ValueError("SENDGRID_API_KEY is not set in the environment.")
else:
    print("found the api key")

app = Flask(__name__)

uri = os.getenv('MONGODB_URI')

client = MongoClient(uri)
db = client['upvoice']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)  # define the life span of the token

jwt = JWTManager(app) # initialize JWTManager

@app.route('/login-user', methods=['POST'])
def login_user():
    data = request.json
    # Check if user already exists in the database
    existing_user = db.users.find_one({'username': data['username']})
    
    if existing_user and hashlib.sha256(data["password"].encode("utf-8")).hexdigest() == existing_user['password']:
        # Update the user's login status or set a variable indicating they are logged in
        access_token = create_access_token(identity=existing_user['username']) # create jwt token
        return jsonify(access_token=access_token), 200
    elif existing_user:
        return jsonify({'message': 'Incorrect password: ' + data['username']}), 400
    else:
        return jsonify({'message': 'Account not found: ' + data['username']}), 404

@app.route('/logout-user', methods=['POST'])
@jwt_required()
def logout_user():
    data = request.json

    # Invalidate the JWT
    current_user = get_jwt_identity() # Get the identity of the current user
    logged_in_user = db.users.find_one({'username' : current_user})

    if not logged_in_user:
        return jsonify({'message': 'User not logged in, thus cannot be logged out: '}), 404
    else: # TODO
        db.users.update_one({'username': logged_in_user['username']}, {'$set': {'logged_in': False}})
        return jsonify({'message': 'User Logged out successfully: ' + logged_in_user['username']}), 200
        # data['username']
    '''
    data = request.json
    # Check if user already exists in the database
    existing_user = db.users.find_one({'username': data['username']})
    
    if existing_user and data['password'] == existing_user['password']:
        # Update the user's login status or set a variable indicating they are logged in
        return jsonify({'message': 'User logged in successfully ' + existing_user['username']}), 200
    elif existing_user:
        return jsonify({'message': 'Incorrect password: ' + data['username']}), 400
    else:
        return jsonify({'message': 'Account not found: ' + data['username']}), 404
    '''

@app.route('/login-stakeholder', methods=['POST'])
def login_stakeholder():
    data = request.json
    # Check if user already exists in the database
    existing_stakeholder = db.stakeholders.find_one({'username': data['username']})
    
    if existing_stakeholder and hashlib.sha256(data["password"].encode("utf-8")).hexdigest() == existing_stakeholder['password']:
        # Update the stakeholder's login status or set a variable indicating they are logged in
        access_token = create_access_token(identity=existing_stakeholder['username']) # create jwt token
        return jsonify(access_token=access_token), 200
    elif existing_stakeholder:
        return jsonify({'message': 'Incorrect password: ' + data['username']}), 400
    else:
        return jsonify({'message': 'Account not found: ' + data['username']}), 404

@app.route('/logout-stakeholder', methods=['POST'], endpoint='logout_stakeholder')
@jwt_required()
def logout_stakeholder():
    data = request.json

    current_stakeholder = get_jwt_identity() # Get the identity of the current user
    logged_in_stakeholder = db.stakeholders.find_one({'username' : current_stakeholder})

    if not logged_in_stakeholder:
        return jsonify({'message': 'User not logged in, thus cannot be logged out: '}), 404
    else: # TODO
        db.users.update_one({'username': logged_in_stakeholder['username']}, {'$set': {'logged_in': False}})
        return jsonify({'message': 'User Logged out successfully: ' + logged_in_stakeholder['username']}), 200
    '''
    # Check if user already exists in the database
    existing_stakeholder = db.stakeholders.find_one({'username': data['username']})
    
    if existing_stakeholder and data['password'] == existing_stakeholder['password']:
        # Update the user's login status or set a variable indicating they are logged in
        db.stakeholders.update_one({'username': data['username']}, {'$set': {'logged_in': True}})
        return jsonify({'message': 'Stakeholder logged in successfully ' + existing_stakeholder['username']}), 200
    elif existing_stakeholder:
        return jsonify({'message': 'Incorrect password: ' + data['username']}), 400
    else:
        return jsonify({'message': 'Account not found: ' + data['username']}), 404
    '''


@app.route('/add-user', methods=['POST'])
def add_user():
    data = request.json
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Missing username or email'}), 400

    # Check if the user already exists
    if db.users.find_one({'username': data['username']}):
        return jsonify({'error': 'User already exists'}), 409

    # Create the new user
    new_user = {
        'username': data['username'],
        'email': data['email'],
        'email_provided': data['email_provided'], # TODO: flag to check if the email has been provided and thatwe can send an email there. 
        'password': data['password'],
        'decibels': 10,
        'voices': [],  # Initialize an empty list of voices
    }

    new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest() # encrypt password

    
    result = db.users.insert_one(new_user)
    new_user['_id'] = str(result.inserted_id)
    return jsonify({'message': 'User created successfully', 'user': new_user}), 201


@app.route('/add-stakeholder', methods=['POST']) 
def add_stakeholder():
    data = request.json
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Missing username or email'}), 400

    # Check if the user already exists
    if db.stakeholders.find_one({'username': data['username']}):
        return jsonify({'error': 'Stakeholder already exists'}), 409

    # Create the new user
    new_stakeholder = {
        'username': data['username'],
        'email': data['email'],
        'company': data['company'], 
        'password': data['password'],
        'voices': [],  # Initialize an empty list of voices
    }

    new_stakeholder["password"] = hashlib.sha256(new_stakeholder["password"].encode("utf-8")).hexdigest() 

    result = db.stakeholders.insert_one(new_stakeholder)
    new_stakeholder['_id'] = str(result.inserted_id)
    return jsonify({'message': 'Stakeholder created successfully', 'user': new_stakeholder}), 201

#email, name, company, password, leave voices as is 

@app.route('/view-user-voices', methods=['POST'])
@jwt_required()
def view_user_voices():
    current_user = get_jwt_identity() # Get the identity of the current user
    user = db.users.find_one({'username' : current_user})
    
    if not user:
        return jsonify({'message': 'No user currently logged in'}), 404
    
    voices = list(db.voices.find({'citizen_username': user['username']}))

    # print(voices)
    
    # conversion into renderable struct for frontend
    voices_list = [{
        'id': str(voice['_id']),
        'citizen_username': voice['citizen_username'],
        'company': voice['company'],
        'stakeholder_email': voice['stakeholder_email'],
        'voice_summary': voice['voice_summary'],
        'email': voice['email'],
        'subject': voice['subject'],
        'urgency': voice['urgency'],
        'sector': voice['sector'],
        'status': voice['status'],
        'id': voice['_id']
    } for voice in voices]
    
    return jsonify({'user': user['username'], 'voices': voices_list}), 200


@app.route('/view-stakeholder-voices', methods=['POST'])
@jwt_required()
def view_stakeholder_voices():
    current_stakeholder = get_jwt_identity() # Get the identity of the current user
    stakeholder = db.stakeholders.find_one({'email' : current_stakeholder})
    
    if not stakeholder:
        return jsonify({'message': 'No stakeholder currently logged in'}), 404
    
    voices = list(db.voices.find({'stakeholder_email': stakeholder['email']}))

    # print(voices)
    
    # conversion into renderable struct for frontend
    voices_list = [{
        'citizen_username': voice['citizen_username'],
        'company': voice['company'],
        'stakeholder_email': voice['stakeholder_email'],
        'voice_summary': voice['voice_summary'],
        'email': voice['email'],
        'subject': voice['subject'],
        'urgency': voice['urgency'],
        'sector': voice['sector'],
        'status': voice['status'],
        'id': voice['_id']
    } for voice in voices]
    
    return jsonify({'stakeholder': stakeholder['email'], 'voices': voices_list}), 200

@app.route('/delete-voice', methods=['DELETE'])
@jwt_required()
def delete_voice():
    data = request.json
    voice_id = data.get('id')

    if not voice_id:
        return jsonify({'message': 'Voice ID is required'}), 400

    try:
        # Attempt to convert the provided ID to a valid ObjectId
        oid = ObjectId(voice_id)
    except InvalidId:
        return jsonify({'message': 'Invalid voice ID'}), 400
    
    # Check if the voice exists and delete it
    result = db.voices.delete_one({'_id': oid})
    
    if result.deleted_count == 0:
        return jsonify({'message': 'No voice found with the provided ID'}), 404
    
    return jsonify({'message': 'Voice deleted successfully'}), 200

@app.route('/change-voice-status', methods=['POST'])
@jwt_required()
def change_voice_status():
    data = request.json
    voice_id = data.get('id')
    new_status = data.get('new_status')

    if not voice_id:
        return jsonify({'message': 'Voice ID is required'}), 400

    try:
        # Attempt to convert the provided ID to a valid ObjectId
        oid = ObjectId(voice_id)
    except InvalidId:
        return jsonify({'message': 'Invalid voice ID'}), 400
    
    # Change cur_voice's status to change_status
    result = db.voices.find_one_and_update(
        {'_id': oid},
        {'$set': {'status': new_status}},
        return_document=True
    )
    
    if result is None:
        return jsonify({'message': 'No voice found with the provided ID'}), 404
    
    voice = db.voices.find_one(
    {'_id': oid}
    )

    message = Mail(
    from_email=os.getenv('SENDGRID_FROM_EMAIL'),
    to_emails=voice['stakeholder_email'],
    subject='Status of voice changed to: ' + voice['status'],
    html_content='<h1>Title for Email</h1> <br> <strong>Line of Emphasis Here</strong> Please do not reply to this email.')
    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print("SUCCESS!")
    except Exception as e:
        print("EXCEPTION!")
        print(str(e))
    
    return jsonify({'message': 'Voice status updated successfully'}), 200

@app.route('/add-voice', methods=['POST'])
@jwt_required()
def add_voice():

    current_user = get_jwt_identity() # Get the identity of the current user
    user = db.users.find_one({'username' : current_user})

    data = request.json
    username = user['username']

    company = data['company']

    sector = data['sector']

    summary = data['summary']

    # Find the associated email to send it to (based on the company!)
    stakeholder = db.stakeholders.find_one({'company': company})
    stakeholder_email = stakeholder['email']

    if not user:
        return jsonify({"message": "User does not exist"}), 404
    voice = {
        'citizen_username': username,
        'company': company,
        'sector': sector,
        'stakeholder_email': stakeholder_email,
        'voice_summary': summary,
        'email': "",
        'subject': "",
        'urgency': 50,
        'status': "unresolved"
    }

    # Call Gemini here to fill out the email, subject and urgency (50 is just the default)

    # use Sendgrid/Fetch in this endpoint to send the email
    message = Mail(
    from_email=os.getenv('SENDGRID_FROM_EMAIL'),
    to_emails=voice['stakeholder_email'],
    subject='Subject line from LLM here ' + sector,
    html_content='<h1>Title for Email</h1> <br> <strong>Line of Emphasis Here</strong> Please do not reply to this email.')
    print(voice['stakeholder_email'])
    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print("SUCCESS!")
    except Exception as e:
        print("EXCEPTION!")
        print(str(e))

    # Store into collection called voices
    db.voices.insert_one(voice)
    return jsonify({'message': 'Voice submitted successfully'}), 201
    


if __name__ == '__main__':
    app.run(debug=True)