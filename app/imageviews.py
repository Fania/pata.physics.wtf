from flask import render_template, request
from app import app
from imagesurfer import getimages


@app.route('/images')
def images():
    return render_template('images.html')


@app.route('/imageresults', methods=['GET', 'POST'])
def imageresults():

    query = request.form['query']

    print(request.form['img_choice'])
    if request.form['img_choice']:
        choice = request.form['img_choice']
    else:
        choice = 'Bing'

    if request.method == 'GET':
        print 'imageresults get: ', query
    else:
        # request was a POST
        print 'imageresults post: ', query

        images_imgs, translations = getimages(query, choice)
        images_len = len(images_imgs)

        return render_template('imageresults.html', **locals())
