from flask.cli import FlaskGroup
from os.path import join, dirname
from app import create_app
from app.model import db
from flask_migrate import Migrate
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = create_app()
app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)