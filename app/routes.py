from flask import render_template
from app import app


@app.route('/')  # Decorators create association between  '/', '/index' and function below
@app.route('/index')
def index():
    user = {'username': 'Dana'}
    return render_template('index.html', title='Home', user = user)