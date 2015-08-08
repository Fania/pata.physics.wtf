from flask import render_template, request
from app import application
from imagesurfer import getimages


@application.route('/images')
def images():
    return render_template('images.html')


@application.route('/imageresults', methods=['GET', 'POST'])
def imageresults():

    query = request.form['query']

    if request.method == 'GET':
        print 'imageresults get: ', query
    else:
        # request was a POST
        print 'imageresults post: ', query

        images_imgs, translations = getimages(query)
        images_len = len(images_imgs)

        return render_template('imageresults.html', **locals())
