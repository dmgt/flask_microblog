from app import app


@app.route('/')  # Decorators create association between  '/', '/index' and function below
@app.route('/index')
def index():
    return "Hello World"
