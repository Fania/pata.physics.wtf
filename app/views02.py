from flask import render_template, url_for, request
from app import app

from surfer02 import *

@app.route('/p02')
def p02():
    return render_template('p02.html')


@app.route('/p02results', methods=['GET', 'POST'])
def p02results():

    query = request.form['query']

    if request.method == 'GET':
        print 'p02results get: ', query  # data['query']
        # return render_template('p01results.html', q)
    else:
        #request was a POST
        print 'p02results post: ', query  # data['query']
        # qx = getResults(q)

       # IMAGES
        images_imgs, translations = images(query)
        images_len = len(images_imgs)

        #print data
        return render_template('p02results.html', **locals())
