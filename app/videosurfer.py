import requests
from imagesurfer import pataphysicalise
#############################################

# YOUTUBE SEARCH API
yt_key = 'AIzaSyDPZlMpFVZUBfhD4ycjfUZzCR_mVDP59jY'


def getvideos(query):
    out = []
    words = query.split()

    translations = pataphysicalise(words)
    patawords = translations[2]

    b0 = "https://www.googleapis.com/youtube/v3/search?"
    b1 = "&order=viewCount&part=snippet&"
    b2 = "q=%s" % patawords
    b3 = "&type=video&key=%s" % yt_key
    b4 = "&maxResults=10&safeSearch=strict"
    yturl = ''.join([b0, b1, b2, b3, b4])

    vids = requests.get(yturl)

    for i in vids.json()['items']:
        vidtitle = i['snippet']['title']
        vidthumb = i['snippet']['thumbnails']['default']['url']
        vidid = i['id']['videoId']
        out.append((vidtitle, vidthumb, vidid))

    return out, translations
