from flask import render_template, url_for, request
from app import app
from videosurfer import *
from imagesurfer import transent, pataphysicalise
import time


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
        date = time.strftime("%c")
        t = 'videoresults post: '+ date+' ['+ query +']' +'\n'
        with open("log.txt", "a") as mylog:
            mylog.write(t)


        # qx = getResults(q)

        # VIDEOS
        # translations = transent(query)
        # print('trans ', translations)

        # transplit = translations[2].split(' ')
        # pata = pataphysicalise(transplit)


        videos_vids, translations = getvideos(query)
        videos_len = len(videos_vids)

        #print data
        return render_template('videoresults.html', **locals())
