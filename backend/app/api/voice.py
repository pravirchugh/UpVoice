import json
import os
import pandas as pd

import google.generativeai as genai

from flask import Blueprint, request, jsonify
from flask import current_app as app
from app.model import db
from bson.objectid import ObjectId
from sendgrid import SendGridAPIClient
from bson.errors import InvalidId
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from flask_jwt_extended import jwt_required, get_jwt_identity

voice = Blueprint("voice", __name__, url_prefix='/voice')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')


@voice.route('/delete-voice', methods=['DELETE'])
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


@voice.route('/add-voice', methods=['POST'])
@jwt_required()
def add_voice():

    current_user = get_jwt_identity() # Get the identity of the current user
    user = db.users.find_one({'username' : current_user})

    if not user:
        return jsonify({"message": "User does not exist"}), 404

    data = request.json
    username = user['username']

    company = data['company']

    sector = data['sector']

    summary = data['summary']

    # Find the associated email to send it to (based on the company!)
    stakeholder = db.stakeholders.find_one({'company': company})
    

    if not stakeholder:
        return jsonify({"message": "Stakeholder does not have account yet"}), 404
    
    stakeholder_email = stakeholder['email']

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
    email_body = model.generate_content("Generate an email complaint, in HTML format with HTML elements from a citizen to an investor at " + company + ". The category of the issue is " + sector + ". Please include and expand on this summary of the citizen's grievance: " + summary + ". Do not include any placeholders AT ALL, and do not make personal requests. Instead, make emotional calls to action for the company as a whole. Do not return any other information besides the email in HTML format. ")
    print(email_body.text)

    email_subject = model.generate_content("Generate an email complaint from a citizen to an investor at " + company + ". The category of the issue is " + sector + ". Please include and expand on this summary of the citizen's grievance: " + summary + ". Return ONLY the subject of the email, nothing else.")
    print(email_subject.text)

    # use Sendgrid/Fetch in this endpoint to send the email
    message = Mail(
    from_email=os.getenv('SENDGRID_FROM_EMAIL'),
    to_emails=voice['stakeholder_email'],
    subject=email_subject.text,
    html_content=email_body.text[7:] + ' Please do not reply to this email.')
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

    voice = {
        'citizen_username': username,
        'company': company,
        'sector': sector,
        'stakeholder_email': stakeholder_email,
        'voice_summary': summary,
        'email': email_body.text[7:],
        'subject': email_subject.text,
        'urgency': 50,
        'status': "unresolved"
    }

    # Store into collection called voices
    db.voices.insert_one(voice)
    return jsonify({'message': 'Voice submitted successfully'}), 201