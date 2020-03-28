import requests
from .imagesurfer import pataphysicalise, transent
from .keys import *
#############################################


def getvideos(query):
    out = []
    translations = transent(query)
    # print('trans ', translations)
    transplit = str(translations[2]).split(' ')
    tmp = pataphysicalise(transplit)

    b0 = "https://www.googleapis.com/youtube/v3/search?"
    b1 = "&order=viewCount&part=snippet&"
    b3 = "&type=video&key=%s" % youtube_k
    b4 = "&maxResults=10&safeSearch=strict"

    for x in tmp:
        y = ' '.join(x)
        b2 = "q=%s" % translations[2]
        yturl = ''.join([b0, b1, b2, b3, b4])
        vids = requests.get(yturl)
        if vids.json()['items']:
            for i in vids.json()['items']:
                vidtitle = i['snippet']['title']
                vidthumb = i['snippet']['thumbnails']['default']['url']
                vidid = i['id']['videoId']
                out.append((vidtitle, vidthumb, vidid))
            break
        else:
            out = []
    return out, translations
