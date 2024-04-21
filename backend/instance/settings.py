import os

SECRET_KEY=os.environ['SECRET_KEY']
DB_HOST=os.environ['DB_HOST']
DATABASE_NAME=os.environ['DATABASE_NAME']
MONGODB_URI = "mongodb://localhost:27017/%s" % (DATABASE_NAME)
MONGO_DB_DATABASE_URI = "mongodb+srv://pravirc:pravirc1@clustermain.jwpbamn.mongodb.net/?retryWrites=true&w=majority"
GEMINI_API_KEY=os.environ['GEMINI_API_KEY']
SENDGRID_API_KEY=os.environ['SENDGRID_API_KEY']
SENDGRID_FROM_EMAIL=os.environ['SENDGRID_FROM_EMAIL']