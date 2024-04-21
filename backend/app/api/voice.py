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

voice = Blueprint("voice", __name__, url_prefix='/voice')

@voice.route('/delete', methods=['DELETE'])
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


@voice.route('/add', methods=['POST'])
def add_voice():
    data = request.json
    username = data['username']

    company = data['company']

    sector = data['sector']

    summary = data['summary']

    user = db.users.find_one({'username': username})

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