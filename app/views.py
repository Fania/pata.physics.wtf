from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/basheau')
def basheau():
    return render_template('basheau.html')


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    # raise
    return render_template('errors.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    print(error)
    # raise
    return render_template('errors.html'), 500


@app.errorhandler(400)
def bad_request(error):
    print(error)
    # raise
    return render_template('errors.html'), 400
