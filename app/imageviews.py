from flask import render_template, request
from app import app
from imagesurfer import getimages, transent, pataphysicalise


@app.route('/images')
def images():
    return render_template('images.html')


@app.route('/imageresults', methods=['GET', 'POST'])
def imageresults():

    oldquery = request.form['query']
    # print('oldquery ', oldquery)
    choice = request.form['img_choice']
    # print('choice ', choice)

    trans = transent(oldquery)
    # print('trans ', trans)

    pata = pataphysicalise(trans[2])
    # print('pata ', pata)

    query = pata[0][0]
    # print('query ', query)

    if request.method == 'GET':
        print 'imageresults get: ', query, choice
    else:
        print 'imageresults post: ', query, choice

        # images_imgs, translations = getimages(query, choice)
        # images_len = len(images_imgs)

        # Javascript Img works but only with translations
        images_imgs, translations = [], trans
        images_len = len(images_imgs)

        # Javascript with full pataphysicalisation
        # images_imgs, translations = [], trans
        # images_len = len(images_imgs)

        return render_template('imageresults.html', **locals())
