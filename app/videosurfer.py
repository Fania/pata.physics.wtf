from flask import url_for
from requests.auth import HTTPBasicAuth
from microsofttranslator import Translator
import gdata.youtube.service as yt
import requests
# import unicodedata as ud
import textsurfer

#############################################

# PROTOTYPE 03 - VIDEO

#############################################

# MICROSOFT TRANSLATE
microsoft_id = 'patalator'
microsoft_secret = 'IXfoWZgfMnQ6JFe9UmWcbGxoum+kr6DwFefNh1bFhcM='

# BING VIDEO SEARCH
base = 'https://api.datamarket.azure.com/Bing/Search/'
key = 'KxnH3+uL1TGRJkGlQ5gg7Dwri6GfV121ezf27TRbvUY='


def pataphysicalise(word):

    translator = Translator(microsoft_id, microsoft_secret)
    syzygy_words = textsurfer.syzygy(word)
    if syzygy_words:
        syzword = syzygy_words.pop()
    else:
        syzword = word
    # Pataphysicalisation !!
    french = translator.translate(syzword, "fr")
    japanese = translator.translate(french, "ja")
    patawords = translator.translate(japanese, "en")
    translations = (french, japanese, patawords)
    return translations


def getvideos(word):
    out = []

    translations = pataphysicalise(word)
    patawords = translations[2]

    # YOUTUBE
    client = yt.YouTubeService()
    query = yt.YouTubeVideoQuery()
    query.vq = patawords
    query.max_results = 10
    query.start_index = 1
    query.racy = 'exclude'
    query.orderby = 'relevance'
    query.safeSearch = 'strict'
    query.format = '5'

    feed = client.YouTubeQuery(query)

    for entry in feed.entry:
        title = entry.media.title.text
        tags = entry.media.keywords.text
        author = entry.author
        url = entry.GetSwfUrl()
        thumb = entry.media.thumbnail[0].url
        out.append((title, thumb, url))

    # CHECK CODE BELOW!!!!
    ## BING VIDEOS
    #params = "Video?$format=json&VideoFilters='Aspect:Square'&$top=5&Query='%s'" % #patawords
    ## &ImageFilters='Size:Small+Aspect:Square'
    #url = base + params
    #bing_img = requests.get(url, auth=HTTPBasicAuth(None, key))
    #for result in bing_img.json['d']['results']:
    #    phototitle = ud.normalize('NFKD', result['Title']).encode('ascii', 'ignore')
    #    photothumb = result['Thumbnail']['MediaUrl']
    #    photolink = result['SourceUrl']
    #    out.append((phototitle, photothumb, photolink))

    return out, translations
