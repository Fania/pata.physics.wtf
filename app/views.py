from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors.html'), 500


@app.errorhandler(400)
def bad_request(error):
    return render_template('errors.html'), 400
