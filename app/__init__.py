from flask import Flask
from config import Config  # From config.py

app = Flask(__name__)  # Create application object
app.config.from_object(Config)

from app import routes  # Imported at end to avoid circular imports
