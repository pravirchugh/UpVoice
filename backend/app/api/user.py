import json
import pandas as pd
from flask import Blueprint, request, jsonify
from flask import current_app as app
from app.model import db

user = Blueprint("user", __name__, url_prefix='/user')

@user.route('/view-voices', methods=['POST'])
def view_user_voices():
    user = db.users.find_one({'logged_in': True})
    
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
        'status': voice['status']
    } for voice in voices]
    
    return jsonify({'user': user['username'], 'voices': voices_list}), 200