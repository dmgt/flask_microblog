from flask import Flask
from config import Config  # From config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)  # Create application object
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)

from app import routes, models  # Imported at end to avoid circular imports
                                # models defines structre of db
