import sys
print(sys.executable)

from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

uri = "mongodb+srv://pravirc:pravirc1@cluster0.o07b6ry.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client['upvoice']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route('/login-user', methods=['POST'])
def login_user():
    data = request.json
    # Check if user already exists in the database
    existing_user = db.users.find_one({'username': data['username']})
    
    if existing_user and data['password'] == existing_user['password']:
        # Update the user's login status or set a variable indicating they are logged in
        db.users.update_one({'username': data['username']}, {'$set': {'logged_in': True}})
        return jsonify({'message': 'User logged in successfully ' + existing_user['username']}), 200
    elif existing_user:
        return jsonify({'message': 'Incorrect password: ' + data['username']}), 400
    else:
        return jsonify({'message': 'Account not found: ' + data['username']}), 404

@app.route('/logout-user', methods=['POST'])
def logout_user():
    data = request.json
    # Check if user already exists in the database
    existing_user = db.users.find_one({'username': data['username']})
    
    if existing_user and data['password'] == existing_user['password']:
        # Update the user's login status or set a variable indicating they are logged in
        db.users.update_one({'username': data['username']}, {'$set': {'logged_in': True}})
        return jsonify({'message': 'User logged in successfully ' + existing_user['username']}), 200
    elif existing_user:
        return jsonify({'message': 'Incorrect password: ' + data['username']}), 400
    else:
        return jsonify({'message': 'Account not found: ' + data['username']}), 404


@app.route('/add-voice', methods=['POST'])
def add_voice():
    data = request.json
    username = data['username']

    company = data['company']

    summary = data['summary']

    user = db.users.find_one({'username': username})

    # Find the associated email to send it to (based on the company!) TODO
    # stakeholder = db.stakeholders.find_one({'company': company})
    # stakeholder_email = stakeholder['email']

    stakeholder_email = "stakeholder@stakeholder_company.com"

    if not user:
        return jsonify({"message": "User does not exist"}), 404
    voice = {
        'citizen_username': username,
        'company': company,
        'stakeholder_email': stakeholder_email,
        'voice_summary': summary,
        'email': "",
        'subject': "",
        'urgency': 50,
        'status': "unresolved"
    }

    # Call Gemini here to fill out the email, subject and urgency (50 is just the default)

    # use Mailchimp in this endpoint to send the email

    # Store into collection called voices
    db.voices.insert_one(voice)
    return jsonify({'message': 'Voice submitted successfully'}), 201



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
        'email_provided': data['email_provided'], # flag to check if the email has been provided and thatwe can send an email there. 
        'password': data['password'],
        'voices': [],  # Initialize an empty list of voices
    }
    result = db.users.insert_one(new_user)
    new_user['_id'] = str(result.inserted_id)
    return jsonify({'message': 'User created successfully', 'user': new_user}), 201

if __name__ == '__main__':
    app.run(debug=True)