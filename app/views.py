from flask import render_template, url_for, request

from app import app
from surfer01 import *


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/p01', methods=['GET', 'POST'])
def p01():
    if request.method == 'GET':
        print 'p01 get'
        return render_template('p01.html')
    else:
        #request was a POST
        q = request.form['query']
        print 'p01 post: ', q
        return redirect(url_for('p01results.html'), query=q)


@app.route('/p01results', methods=['GET', 'POST'])
def p01results():
    # Gets the query from the url
    # query = request.args.get('query', '')
    # print 'query: ', query

    if request.method == 'GET':
        q = request.form['query']
        print 'p01results get: ', q
        # return render_template('p01results.html', q)
    else:
        #request was a POST
        q = request.form['query']
        print 'p01results post: ', q
        return render_template('p01results.html', query=q)

    # error = False
    # if query:
    #     if not query:
    #         error = True
    #     else:

    #         # SESSIONS
    #         # pop(key), keys(), items(), get(key), clear(), flush()
    #         # s = request.session
    #         # s.set_expiry(120)
    #         # if 'queries' in s.keys():
    #         #     s['queries'].append(query)
    #         #     #if len(s['queries']) > 9:
    #         #     #    s['queries'].pop([0])
    #         # else:
    #         #     s['queries'] = [query]
    #         # s.save()
    #         # print s.session_key, s.get_expiry_age(), s.get_expire_at_browser_close()
    #         # print 's:', s.items()

    #         # CLINAMEN
    #         sens = dict([])
    #         pre_sens = dict([])
    #         post_sens = dict([])
    #         clinamen_words = clinamen(query, 2)
    #         clinamen_len = len(clinamen_words)
    #         for r in clinamen_words:
    #             if len(pre_sentence(r)) > 0:
    #                 pre_sens[r] = pre_sentence(r)
    #             if len(post_sentence(r)) > 0:
    #                 post_sens[r] = post_sentence(r)
    #             if len(find_sentence(r)) > 0:
    #                 sens[r] = find_sentence(r)
    #         # SYZYGY
    #         syssens = dict([])
    #         pre_syssens = dict([])
    #         post_syssens = dict([])
    #         syzygy_words = syzygy(query)
    #         syzygy_len = len(syzygy_words)
    #         for r in syzygy_words:
    #             if len(pre_sentence(r)) > 0:
    #                 pre_syssens[r] = pre_sentence(r)
    #             if len(post_sentence(r)) > 0:
    #                 post_syssens[r] = post_sentence(r)
    #             if len(find_sentence(r)) > 0:
    #                 syssens[r] = find_sentence(r)
    #         # ANTINOMY
    #         antisens = dict([])
    #         pre_antisens = dict([])
    #         post_antisens = dict([])
    #         antinomy_words = antinomy(query)
    #         antinomy_len = len(antinomy_words)
    #         for r in antinomy_words:
    #             if len(pre_sentence(r)) > 0:
    #                 pre_antisens[r] = pre_sentence(r)
    #             if len(post_sentence(r)) > 0:
    #                 post_antisens[r] = post_sentence(r)
    #             if len(find_sentence(r)) > 0:
    #                 antisens[r] = find_sentence(r)
    #                 #print antisens[r]

    #         return render_template('p01results.html')
    # return render_template('p01results.html', error=error)


@app.route('/p02')
def p02():
    return render_template('p02.html')


@app.route('/p03')
def p03():
    return render_template('p03.html')
