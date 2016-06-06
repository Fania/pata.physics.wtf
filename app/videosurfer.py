import requests
from imagesurfer import pataphysicalise, transent
#############################################

# YOUTUBE SEARCH API
yt_key = 'AIzaSyDPZlMpFVZUBfhD4ycjfUZzCR_mVDP59jY'


def getvideos(query):
    out = []
    trans = ''
    words = query.split()

    tmp = pataphysicalise(words)

    b0 = "https://www.googleapis.com/youtube/v3/search?"
    b1 = "&order=viewCount&part=snippet&"
    b3 = "&type=video&key=%s" % yt_key
    b4 = "&maxResults=10&safeSearch=strict"

    for x in tmp:
        y = ' '.join(x)
        z = transent(y)
        b2 = "q=%s" % z[2]
        yturl = ''.join([b0, b1, b2, b3, b4])
        vids = requests.get(yturl)
        if vids.json()['items']:
            trans = z
            for i in vids.json()['items']:
                vidtitle = i['snippet']['title']
                vidthumb = i['snippet']['thumbnails']['default']['url']
                vidid = i['id']['videoId']
                out.append((vidtitle, vidthumb, vidid))
            break
        else:
            out = []
    return out, trans
