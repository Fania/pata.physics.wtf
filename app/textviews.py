from flask import render_template, request
from app import app
from textsurfer import clinamen, syzygy, antinomy, calc_all


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
        # [(title, (pre, word, post), algorithm), ...]

        # clin_words = ['hello', 'world', 'fania', 'loves', 'dave']

        clin_sens, clin_words, clin_files, clin_tot = clinamen(query, 2)
        sys_sens, sys_words, sys_files, sys_tot = syzygy(query)
        anti_sens, anti_words, anti_files, anti_tot = antinomy(query)
        print(clin_sens)
        print(sys_sens)
        print(anti_sens)
        all_sens = list(clin_sens | sys_sens | anti_sens)
        all_tot = clin_tot + sys_tot + anti_tot

        all_files = set([f[0] for f in all_sens])
        all_words = set([f[1][1] for f in all_sens])

        lol, part, mx = calc_all(all_sens)

        all_poems = part ** mx  # no of options ^ no of lines

        # print(all_sens)

        # print data
        return render_template('textresults.html', **locals())
