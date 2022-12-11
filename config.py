import os

# Configure the application
DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_key"
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
