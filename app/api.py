from app import app


@app.route('/ping')
def index():
    return 'OK', 200
