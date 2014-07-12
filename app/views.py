from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/p02')
def p02():
    return render_template('p02.html')


@app.route('/p03')
def p03():
    return render_template('p03.html')


@app.route('/about')
def about():
    return render_template('about.html')
