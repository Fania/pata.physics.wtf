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

    translations = transent(oldquery)
    print('trans ', translations)

    transplit = translations[2].split(' ')
    pata = pataphysicalise(transplit)
    print('pata ', pata)

    if request.method == 'GET':
        print 'imageresults get: ', 'test', choice
    else:
        print 'imageresults post: ', 'test', choice

        # images_imgs, trans = getimages(pata, choice)
        # images_len = len(images_imgs)

        # Javascript Img works but only with translations
        images_imgs, trans = [], translations
        images_len = len(images_imgs)

        # Javascript with full pataphysicalisation
        # images_imgs, translations = [], trans
        # images_len = len(images_imgs)

        return render_template('imageresults.html', **locals())
