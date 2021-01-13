import os

from dotenv import load_dotenv

load_dotenv()

DB_CONNECTION_STRING = os.getenv("DATABASE_URL")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
