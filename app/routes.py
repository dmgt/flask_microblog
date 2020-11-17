from flask import render_template
from app import app


@app.route('/')  # Decorators create association between  '/', '/index' and function below
@app.route('/index')
def index():
    user = {'username': 'Dana'}
    posts = [
        {
            'author': {'username': 'Saima'},
            'body': 'Today is a beautiful fall day!'
        },
        {
            'author': {'username': 'Jose'},
            'body': 'I am learning CSS!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)