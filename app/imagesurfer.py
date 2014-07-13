from flask import url_for
from requests.auth import HTTPBasicAuth
from microsofttranslator import Translator
import flickrapi
import requests
# import unicodedata as ud
import textsurfer
#############################################

# PROTOTYPE 02 - IMAGES

#############################################

# MICROSOFT TRANSLATE
microsoft_id = 'patalator'
microsoft_secret = 'IXfoWZgfMnQ6JFe9UmWcbGxoum+kr6DwFefNh1bFhcM='

# FLICKR
api_key = '9a9ab31b6a0003ab43b64088230eb120'

# BING IMAGE SEARCH
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


def getimages(word):
    out = []

    translations = pataphysicalise(word)
    patawords = translations[2]

    # FLICKR
    flickr = flickrapi.FlickrAPI(api_key)
    photos = flickr.photos_search(text=patawords, per_page='10', safe_search='1')
    #owners = set()
    for photo in photos[0]:
        photoid = photo.attrib['id']
        phototitle = photo.attrib['title']
        photoowner = photo.attrib['owner']
        photoSizes = flickr.photos_getSizes(photo_id=photoid)
        photothumb = photoSizes[0][1].attrib['source']
        photolink = "http://www.flickr.com/photos/%s/%s" % (photoowner, photoid)
        # if photoowner not in owners and len(owners) < 10:
        #     owners.add(photoowner)
        out.append((phototitle, photothumb, photolink))

    # BING IMAGES
    # params = "Image?$format=json&ImageFilters='Aspect:Square'&$top=5&Query='%s'" % patawords
    # # &ImageFilters='Size:Small+Aspect:Square'
    # url = base + params
    # bing_img = requests.get(url, auth=HTTPBasicAuth(None, key))
    # for result in bing_img.json['d']['results']:
    #     # phototitle = ud.normalize('NFKD', result['Title']).encode('ascii', 'ignore')
    #     phototitle = result['Title']
    #     photothumb = result['Thumbnail']['MediaUrl']
    #     photolink = result['SourceUrl']
    #     out.append((phototitle, photothumb, photolink))

    return out, translations
