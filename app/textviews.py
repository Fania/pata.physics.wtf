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
        flen = []
        pp_sens = defaultdict(list)
        clinamen_words = clinamen(query, 2)
        clinamen_len = len(clinamen_words)
        print('clinamen_words', clinamen_words)
        # print('pre', len(pp_sens), pp_sens)
        for r in clinamen_words:
            files = sear(r)
            print(r, 'files: ', files)
            for e in files:
                flen.append(e)
                # print('inside files loop', r, e)
                # print(len(pp_sent(r, e)))
                if len(pp_sent(r, e)) > 0:
                    # print(pp_sent(r, e))
                    pp_sens[r].append(pp_sent(r, e))
                # else:
                    # print('fail pre')
                # print('end of loop')
        # print('pp_sens', pp_sens)
        tflen = set(flen)
        print('FINAL tflen:', tflen)

        # SYZYGY
        # syssens = dict([])
        # pre_syssens = dict([])
        # post_syssens = dict([])
        # syzygy_words = syzygy(query)
        # syzygy_len = len(syzygy_words)
        # for r in syzygy_words:
        #     if len(pre_sentence(r)) > 0:
        #         pre_syssens[r] = pre_sentence(r)
        #     if len(post_sentence(r)) > 0:
        #         post_syssens[r] = post_sentence(r)
        #     if len(find_sentence(r)) > 0:
        #         syssens[r] = find_sentence(r)
        # ANTINOMY
        # antisens = dict([])
        # pre_antisens = dict([])
        # post_antisens = dict([])
        # antinomy_words = antinomy(query)
        # antinomy_len = len(antinomy_words)
        # for r in antinomy_words:
        #     if len(pre_sentence(r)) > 0:
        #         pre_antisens[r] = pre_sentence(r)
        #     if len(post_sentence(r)) > 0:
        #         post_antisens[r] = post_sentence(r)
        #     if len(find_sentence(r)) > 0:
        #         antisens[r] = find_sentence(r)
        #         print antisens[r]

        # print data
        return render_template('textresults.html', **locals())
