from flask import render_template, url_for, request
from app import app

from surfer03 import *


@app.route('/p03')
def p03():
    return render_template('p03.html')


@app.route('/p03results', methods=['GET', 'POST'])
def p03results():

    query = request.form['query']

    if request.method == 'GET':
        print 'p03results get: ', query  # data['query']
        # return render_template('p01results.html', q)
    else:
        #request was a POST
        print 'p03results post: ', query  # data['query']
        # qx = getResults(q)

        # VIDEOS
        videos_vids, translations = videos(query)
        videos_len = len(videos_vids)

        #print data
        return render_template('p03results.html', **locals())
