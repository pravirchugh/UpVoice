from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['upvoice']

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Check if user already exists in the database
    existing_user = db.users.find_one({'id': data['id']})
    
    if existing_user:
        # Update the user's login status or set a variable indicating they are logged in
        db.users.update_one({'id': data['id']}, {'$set': {'logged_in': True}})
        return jsonify({'message': 'User logged in successfully ' + data['id']}), 200
    else:
        # Create a new user
        db.users.insert_one({'id': data['id'], 'logged_in': True})
        return jsonify({'message': 'New user created and logged in successfully ' + data[id]}), 201

@app.route('/add-voice', methods=['POST'])
def submit_voice():
    data = request.json
    # Store into collection called voices
    db.voices.insert_one(data)
    return jsonify({'message': 'Voice submitted successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)