# from flask import url_for
# from requests.auth import HTTPBasicAuth
# from microsofttranslator import Translator
# import gdata.youtube
# import gdata.youtube.service
# import json
import requests
# import unicodedata as ud
# import textsurfer
from imagesurfer import pataphysicalise
#############################################

# BING VIDEO SEARCH API
# base = 'https://api.datamarket.azure.com/Bing/Search/'
# key = 'KxnH3+uL1TGRJkGlQ5gg7Dwri6GfV121ezf27TRbvUY='

# YOUTUBE SEARCH API
yt_key = 'AIzaSyDPZlMpFVZUBfhD4ycjfUZzCR_mVDP59jY'
# yt_service = gdata.youtube.service.YouTubeService()
# yt_service.ssl = True


def getvideos(query):
    print('inside getvideos', query)
    out = []
    words = query.split()

    translations = pataphysicalise(words)
    patawords = translations[2]
    print('patawords', patawords)

    b0 = "https://www.googleapis.com/youtube/v3/search?"
    b1 = "videoDefinition=high&order=viewCount&part=snippet&"
    b2 = "q=%s" % patawords
    b3 = "&type=video&key=%s" % yt_key
    b4 = "&maxResults=10&safeSearch=strict"
    yturl = ''.join([b0, b1, b2, b3, b4])
    print('yturl', yturl)

    vids = requests.get(yturl)
    print(vids)

    for i in vids.json()['items']:
        vidtitle = i['snippet']['title']
        vidthumb = i['snippet']['thumbnails']['default']['url']
        vidid = i['id']['videoId']
        out.append((vidtitle, vidthumb, vidid))
        print(out)

    return out, translations
