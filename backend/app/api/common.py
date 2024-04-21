import json
import pandas as pd
from flask import Blueprint, request, jsonify
from flask import current_app as app
from app.model import db

common = Blueprint("common", __name__, url_prefix='/common')

@common.route('/fetch-company-list', methods=['GET'])
def fetch_company_list():
    companies_collection = db.companies
    companies = list(companies_collection.find({}, {'_id': 0, 'name': 1}))
    response = {
        "status": True,
        "data": companies
    }
    return jsonify(response)

@common.route('/fetch-company-categories', methods=['GET'])
def get_categories():
    companies_collection = db.companies
    categories = companies_collection.distinct('category')
    response = {
        "status": True,
        "data": categories
    }
    return jsonify(response)



# @common.route('/insert-csv-data', methods=['POST'])
# def insert_csv_data():
#     # Read CSV file into a pandas DataFrame
#     csv_data = pd.read_csv('~/Desktop/companies_sorted.csv')
    
#     # Convert DataFrame to a list of dictionaries (each row becomes a dictionary)
#     data = csv_data.to_dict(orient='records')
    
#     # Create or get the collection in MongoDB
#     companies_collection = db.companies  # Assuming "companies" is the name of the collection
    
#     # Insert data into the collection
#     companies_collection.insert_many(data)
    
#     return jsonify({"message": "CSV data inserted successfully into MongoDB collection"})