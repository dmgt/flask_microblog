from flask import Flask


app = Flask(__name__)  # Create application object

from app import routes  # Imported at end to avoid circular imports
