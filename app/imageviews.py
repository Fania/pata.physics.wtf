from flask import render_template, request
from app import app
# from .imagesurfer import transent, pataphysicalise
from .imagesurfer import getFlickrImages, getBingImages, transent, pataphysicalise
import random, time


@app.route('/images')
def images():
    return render_template('images.html')


@app.route('/imageresults', methods=['GET', 'POST'])
def imageresults():

    oldquery = request.form['query']
    choice = request.form['img_choice']

    # print oldquery, choice
    translations = transent(oldquery)
    # print('trans ', translations)

    pata = list(pataphysicalise(translations[2].split(" ")))
    # print('pata ', pata)

    # Get 1 random item from the list of pataphysicalised query terms to run the API call with
    if len(pata) >= 10:
        queries = random.sample(pata, 10)
    else:
        errorList = ['empty','error','null','nothing','zero','nix','mistake','incorrect','invalid','useless']
        errors = random.sample(errorList, 10 - len(pata))
        queries = pata + errors

    if request.method == 'GET':
        print('imageresults get: ', queries, choice)
    else:
        print('imageresults post: ', queries, choice)
        date = time.strftime("%c")
        t = f'imageresults post: {date} {oldquery} [{", ".join(queries)}] {choice}\n'
        with open("log.txt", "a") as mylog:
            mylog.write(t)

        # Using Python API code  
        if choice == 'flickr':
            images_imgs = getFlickrImages(queries)
        else:
            images_imgs = getBingImages(queries)
        trans = translations
        images_len = len(images_imgs)

        return render_template('imageresults.html', **locals())
