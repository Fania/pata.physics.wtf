from flask import render_template, request
from app import app
from textsurfer import clinamen, syzygy, antinomy
from math import factorial


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

        # all_sens structure:
        # {word1: [(title, (pre, word, post), algorithm), ...],
        #  word2: [(title, (pre, word, post), algorithm), ...],
        #  ...
        # }

        # clin_words = ['hello', 'world', 'fania', 'loves', 'dave']

        clin_sens, clin_words, clin_files, clin_tot = clinamen(query, 2)
        sys_sens, sys_words, sys_files, sys_tot = syzygy(query)
        anti_sens, anti_words, anti_files, anti_tot = antinomy(query)

        all_sens = clin_sens.copy()
        all_sens.update(sys_sens), all_sens.update(anti_sens)

        all_words = clin_words | sys_words | anti_words
        all_files = clin_files | sys_files | anti_files
        all_tot = clin_tot + sys_tot + anti_tot

        all_poems = factorial(all_tot)

        # print data
        return render_template('textresults.html', **locals())
