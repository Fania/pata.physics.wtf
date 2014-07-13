from flask import render_template, url_for, request
from app import app
from videosurfer import *


@app.route('/videos')
def videos():
    return render_template('videos.html')


@app.route('/videoresults', methods=['GET', 'POST'])
def videoresults():

    query = request.form['query']

    if request.method == 'GET':
        print 'videoresults get: ', query  # data['query']
        # return render_template('p01results.html', q)
    else:
        #request was a POST
        print 'videoresults post: ', query  # data['query']
        # qx = getResults(q)

        # VIDEOS
        videos_vids, translations = getvideos(query)
        videos_len = len(videos_vids)

        #print data
        return render_template('videoresults.html', **locals())
