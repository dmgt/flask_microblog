# Main application module
# Imports app variable (Flask application instance) that is member of app package
from app import app, db
from app.models import User, Post

@app.shell_context_processor #  adds database instance and models to shell session
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}