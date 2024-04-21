import json
import pandas as pd
from flask import Blueprint, request, jsonify
from flask import current_app as app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.model import db
import google.generativeai as genai
import os
import numpy as np

user = Blueprint("user", __name__, url_prefix='/user')

@user.route('/raise-a-voice', methods=['POST'])
@jwt_required()
def raise_a_voice():
    current_user = get_jwt_identity() # Get the identity of the current user
    user = db.users.find_one({'username' : current_user})
    
    if not user:
        return jsonify({'message': 'No user currently logged in'}), 404
    
    data = request.json
    category = data['category']
    company = data['company']
    issue = data['issue']

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    voices = list(db.voices.find({}, {'category': False, 'company': False, 'user_id': False, 'frequency': False }))
    
    model = 'models/embedding-001'

    df = pd.DataFrame(voices)
    df.columns = ['_id','Voices']

    def embed_fn(voices):
        return genai.embed_content(model=model,
                             content=voices,
                             task_type="SEMANTIC_SIMILARITY")["embedding"]

    df['Embeddings'] = df.apply(lambda row: embed_fn(row['Voices']), axis=1)

    query = f'{issue}'
    model = 'models/embedding-001'
    threshold = 0.90
    is_unique_voice = True

    def find_similar_passages(query, dataframe):
        query_embedding = genai.embed_content(model=model,
                                                content=query,
                                                task_type="SEMANTIC_SIMILARITY")
        dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding["embedding"])
        
        indices = [index for index, value in enumerate(dot_products) if value > threshold]

        if(len(indices) > 0):
            is_unique_voice = False

        extracted_ids = df.iloc[indices]['_id'].tolist()

    #     # idx = np.argmax(dot_products)
        return extracted_ids

    similar_ids = find_similar_passages(query, df)

    if(is_unique_voice == True):
        for _id in similar_ids:
            result = db.voices.update_one(
                {'_id': _id},
                {'$inc': {'frequency': 1}}
            )

    # Urgency
    urgent_keywords = ["urgent", "emergency", "critical", "crisis", "immediate", "pressing"]

    embedded_urgency = embed_fn(",".join(urgent_keywords))

    def find_urgency_score(query, embedded_urgency):
        query_embedding = genai.embed_content(model=model,
                                                content=query,
                                                task_type="retrieval_query")
        dot_products = np.dot(np.stack(embedded_urgency), query_embedding["embedding"])
        return dot_products
    
    current_voice_urgency_score = find_urgency_score(issue, embedded_urgency)
 
    prompt = f"""From the given input text, give all the important points which are the problem, urgency and impact. 
                 It should be concise having all the major points. Keep in mind, to not use summary word anywhere in the 
                 response. 
                 issue: {issue}
                 company: {company}
                 category: {category}
                """
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)

    user = db.users.find_one({'username' : current_user})

    document = {
        "user_id": user['_id'],
        "company_name": company,
        "voice": response.text,
        "urgency_score": current_voice_urgency_score,
    }
    
    db.citizen_voices.insert_one(document)

    return jsonify({
        "status": True,
        "message": 'Voice raised successfully'
    })


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

