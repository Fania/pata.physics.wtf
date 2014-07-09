from flask import render_template, url_for, request
from app import app

from surfer01 import *


@app.route('/p01')
def p01():
    return render_template('p01.html')


@app.route('/p01results', methods=['GET', 'POST'])
def p01results():

    query = request.form['query']

    if request.method == 'GET':
        print 'p01results get: ', query  # data['query']
        # return render_template('p01results.html', q)
    else:
        #request was a POST
        print 'p01results post: ', query  # data['query']
        # qx = getResults(q)

       # CLINAMEN
        sens = dict([])
        pre_sens = dict([])
        post_sens = dict([])
        clinamen_words = clinamen(query, 2)
        clinamen_len = len(clinamen_words)
        for r in clinamen_words:
            if len(pre_sentence(r)) > 0:
                pre_sens[r] = pre_sentence(r)
            if len(post_sentence(r)) > 0:
                post_sens[r] = post_sentence(r)
            if len(find_sentence(r)) > 0:
                sens[r] = find_sentence(r)
        # SYZYGY
        syssens = dict([])
        pre_syssens = dict([])
        post_syssens = dict([])
        syzygy_words = syzygy(query)
        syzygy_len = len(syzygy_words)
        for r in syzygy_words:
            if len(pre_sentence(r)) > 0:
                pre_syssens[r] = pre_sentence(r)
            if len(post_sentence(r)) > 0:
                post_syssens[r] = post_sentence(r)
            if len(find_sentence(r)) > 0:
                syssens[r] = find_sentence(r)
        # ANTINOMY
        antisens = dict([])
        pre_antisens = dict([])
        post_antisens = dict([])
        antinomy_words = antinomy(query)
        antinomy_len = len(antinomy_words)
        for r in antinomy_words:
            if len(pre_sentence(r)) > 0:
                pre_antisens[r] = pre_sentence(r)
            if len(post_sentence(r)) > 0:
                post_antisens[r] = post_sentence(r)
            if len(find_sentence(r)) > 0:
                antisens[r] = find_sentence(r)
                #print antisens[r]

        #print data
        return render_template('p01results.html', **locals())
