from flask import render_template, request
from app import app
from imagesurfer import getimages, transent, pataphysicalise
import random


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

    # Get 1 random item from the list of pataphysicalised query terms to run the API call with
    # query = random.sample(pata, 1)[0]
    queries = random.sample(pata, 10)
    print queries

    if request.method == 'GET':
        print 'imageresults get: ', queries, choice
    else:
        print 'imageresults post: ', queries, choice

        # Using Python API code
        # images_imgs, trans = getimages(pata, choice)
        # images_len = len(images_imgs)

        # Using Javascript API code
        images_imgs, trans = [], translations
        images_len = len(images_imgs)


        return render_template('imageresults.html', **locals())
