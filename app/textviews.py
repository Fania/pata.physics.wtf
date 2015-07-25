from flask import render_template, request
from app import app
from textsurfer import *


@app.route('/text')
def text():
    return render_template('text.html')


@app.route('/textresults', methods=['GET', 'POST'])
def textresults():

    query = request.form['query']

    if request.method == 'GET':
        print 'textresults get: ', query  # data['query']
        # return render_template('p01results.html', q)
    else:
        # request was a POST
        print 'textresults post: ', query  # data['query']
        # qx = getResults(q)

        # CLINAMEN
        clin_sens, clin_words, clin_files = clinamen(query, 2)

        # SYZYGY
        # sys_sens, sys_words, sys_files = syzygy(query)

        # ANTINOMY
        # anti_sens, anti_words, anti_files = antinomy(query)

        # print data
        return render_template('textresults.html', **locals())
