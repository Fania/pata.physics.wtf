from flask import render_template, request
from app import app

import random, time


@app.route('/audio')
def audio():
    return render_template('audio.html')

