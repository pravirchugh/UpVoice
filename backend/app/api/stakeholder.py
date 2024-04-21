import json
import os
import pandas as pd

from flask import Blueprint, request, jsonify
from flask import current_app as app
from app.model import db
from bson.objectid import ObjectId
from sendgrid import SendGridAPIClient
from bson.errors import InvalidId
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import google.generativeai as genai

from flask_jwt_extended import jwt_required, get_jwt_identity

stakeholder = Blueprint("stakeholder", __name__, url_prefix='/stakeholder')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@stakeholder.route('/view-stakeholder-voices', methods=['POST'])
@jwt_required()
def view_stakeholder_voices():
    current_stakeholder = get_jwt_identity() # Get the identity of the current user
    stakeholder = db.stakeholders.find_one({'username' : current_stakeholder})
    
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
        'id': str(voice['_id'])
    } for voice in voices]
    
    return jsonify({'stakeholder': stakeholder['email'], 'voices': voices_list}), 200


@stakeholder.route('/change-voice-status', methods=['POST'])
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

    # Call Gemini here to fill out the email, subject -> notification that the voice changed status
    email_body = model.generate_content("Generate an email notification, in HTML format with HTML elements from an investor of " + voice['company'] + " to a citizen who had a complaint against the company. The summary of the complaint was: " + voice['subject'] + " . The status of the complaint has changed to: " + new_status + " . Do not return any other information besides the email in HTML format. ")
    print(email_body.text)

    email_subject = "Status Change: Your voice is now: " + new_status
    


    message = Mail(
    from_email=os.getenv('SENDGRID_FROM_EMAIL'),
    to_emails=voice['stakeholder_email'],
    subject=email_subject,
    html_content=email_body.text[7:] + " Please do not reply to this email.")
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


