# Configuration for the target app
import os

# DB_PASSWORD and API_KEY should be fetched from environment variables
DB_PATH = "test.db"
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'default_password')
API_KEY = os.environ.get('API_KEY', 'default_key')