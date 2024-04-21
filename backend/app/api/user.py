import json
import pandas as pd
from flask import Blueprint, request, jsonify
from flask import current_app as app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.model import db

user = Blueprint("user", __name__, url_prefix='/user')

@user.route('/view-user-voices', methods=['POST'])
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
        'id': str(voice['_id']),  # Convert ObjectId to string
        'citizen_username': voice.get('citizen_username', ''),
        'company': voice.get('company', ''),
        'stakeholder_email': voice.get('stakeholder_email', ''),
        'voice_summary': voice.get('voice_summary', ''),
        'email': voice.get('email', ''),
        'subject': voice.get('subject', ''),
        'urgency': voice.get('urgency', ''),
        'sector': voice.get('sector', ''),
        'status': voice.get('status', '')
    } for voice in voices]
    
    return jsonify({'user': user['username'], 'voices': voices_list}), 200