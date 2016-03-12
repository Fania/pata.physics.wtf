from flask import render_template, request
from app import app
from imagesurfer import getimages, transent


@app.route('/images')
def images():
    return render_template('images.html')


@app.route('/imageresults', methods=['GET', 'POST'])
def imageresults():

    oldquery = request.form['query']
    choice = request.form['img_choice']

    trans = transent(oldquery)
    query = trans[2]

    if request.method == 'GET':
        print 'imageresults get: ', query, choice
    else:
        print 'imageresults post: ', query, choice

        # images_imgs, translations = getimages(query, choice)
        # images_len = len(images_imgs)

        images_imgs, translations = [], trans
        images_len = len(images_imgs)

        return render_template('imageresults.html', **locals())
