from flask import render_template

from app import application


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')


@application.route('/about')
def about():
    return render_template('about.html')


@application.errorhandler(404)
def page_not_found(error):
    return render_template('errors.html'), 404


@application.errorhandler(500)
def internal_server_error(error):
    return render_template('errors.html'), 500


@application.errorhandler(400)
def bad_request(error):
    return render_template('errors.html'), 400
