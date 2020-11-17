from app import app


@app.route('/')  # Decorators create association between  '/', '/index' and function below
@app.route('/index')
def index():
    user = {'username': 'Dana'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
