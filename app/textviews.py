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
        sens = defaultdict(list)
        pre_sens = defaultdict(list)
        post_sens = defaultdict(list)
        clinamen_words = clinamen(query, 2)
        clinamen_len = len(clinamen_words)
        print('clinamen_words', clinamen_words)
        print('pre', len(pre_sens))
        print('post', post_sens)
        print('sens', sens)
        for r in clinamen_words:
            files = sear(r)
            print(r, 'files: ', files)
            for e in files:
                # print('inside files loop', r, e)
                # print(len(pre_sent(r, e)))
                if len(pre_sent(r, e)) > 0:
                    # print(pre_sent(r, e))
                    pre_sens[r].append(pre_sent(r, e))
                # else:
                    # print('fail pre')
                if len(post_sent(r, e)) > 0:
                    # print(post_sent(r, e))
                    post_sens[r].append(post_sent(r, e))
                # else:
                    # print('fail post')
                if len(fsent(r, e)) > 0:
                    # print(fsent(r, e))
                    sens[r].append(fsent(r, e))
                # else:
                    # print('fail full')
                # print('end of loop')
        print(sens)
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
