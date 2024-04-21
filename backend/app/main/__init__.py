from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return "<h1>Flask is running...</h1>"