from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)