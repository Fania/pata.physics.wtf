# from flask import url_for
# from requests.auth import HTTPBasicAuth
# from microsofttranslator import Translator
import gdata.youtube.service as yt
# import requests
# import unicodedata as ud
# import textsurfer
from imagesurfer import pataphysicalise
#############################################

# BING VIDEO SEARCH
# base = 'https://api.datamarket.azure.com/Bing/Search/'
# key = 'KxnH3+uL1TGRJkGlQ5gg7Dwri6GfV121ezf27TRbvUY='


def getvideos(query):
    print('inside getvideos', query)
    out = []
    words = query.split()

    translations = pataphysicalise(words)
    patawords = translations[2]
    print('patawords', patawords)

    # YOUTUBE
    client = yt.YouTubeService()
    print('client', client)
    query = yt.YouTubeVideoQuery()
    print('query', query)
    query.vq = patawords
    query.max_results = 10
    query.start_index = 1
    query.racy = 'exclude'
    query.orderby = 'relevance'
    query.safeSearch = 'strict'
    query.format = '5'
    print('query', query)

    feed = client.YouTubeQuery(query)
    print('feed', feed)

    for entry in feed.entry:
        title = entry.media.title.text
        # tags = entry.media.keywords.text
        # author = entry.author
        url = entry.GetSwfUrl()
        thumb = entry.media.thumbnail[0].url
        out.append((title, thumb, url))

    # CHECK CODE BELOW!!!!
    # BING VIDEOS
    # params = "Video?$format=json&VideoFilters='Aspect:"
    # "Square'&$top=5&Query='%s'" % # patawords
    # &ImageFilters='Size:Small+Aspect:Square'
    # url = base + params
    # bing_img = requests.get(url, auth=HTTPBasicAuth(None, key))
    # for result in bing_img.json['d']['results']:
    #    phototitle = ud.normalize('NFKD', result['Title']).encode('ascii',
    # 'ignore')
    #    photothumb = result['Thumbnail']['MediaUrl']
    #    photolink = result['SourceUrl']
    #    out.append((phototitle, photothumb, photolink))
    return out, translations
