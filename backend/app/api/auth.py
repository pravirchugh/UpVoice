import json
import pandas as pd
from flask import Blueprint, request, jsonify
from flask import current_app as app
from app.model import db

auth = Blueprint("auth", __name__, url_prefix='/auth')

@auth.route('/login-user', methods=['POST'])
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

@auth.route('/logout-user', methods=['POST'])
def logout_user():
    data = request.json

    logged_in_user = db.users.find_one({'logged_in': True})

    if not logged_in_user:
        return jsonify({'message': 'User not logged in, thus cannot be logged out: '}), 404
    else:
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

@auth.route('/login-stakeholder', methods=['POST'])
def login_stakeholder():
    data = request.json
    # Check if user already exists in the database
    existing_stakeholder = db.stakeholders.find_one({'username': data['username']})
    
    if existing_stakeholder and data['password'] == existing_stakeholder['password']:
        # Update the stakeholder's login status or set a variable indicating they are logged in
        db.stakeholders.update_one({'username': data['username']}, {'$set': {'logged_in': True}})
        return jsonify({'message': 'Stakeholder logged in successfully ' + existing_stakeholder['username']}), 200
    elif existing_stakeholder:
        return jsonify({'message': 'Incorrect password: ' + data['username']}), 400
    else:
        return jsonify({'message': 'Account not found: ' + data['username']}), 404

@auth.route('/logout-stakeholder', methods=['POST'])
def logout_stakeholder():
    data = request.json

    logged_in_stakeholder = db.stakeholders.find_one({'logged_in': True})

    if not logged_in_stakeholder:
        return jsonify({'message': 'User not logged in, thus cannot be logged out: '}), 404
    else:
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


@auth.route('/add-user', methods=['POST'])
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
        'voices': [],  # Initialize an empty list of voices
    }
    result = db.users.insert_one(new_user)
    new_user['_id'] = str(result.inserted_id)
    return jsonify({'message': 'User created successfully', 'user': new_user}), 201


@auth.route('/add-stakeholder', methods=['POST']) 
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
    result = db.stakeholders.insert_one(new_stakeholder)
    new_stakeholder['_id'] = str(result.inserted_id)
    return jsonify({'message': 'Stakeholder created successfully', 'user': new_stakeholder}), 201