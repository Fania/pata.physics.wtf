from microsofttranslator import Translator
# import flickrapi
import requests  # BING IMG
from requests.auth import HTTPBasicAuth  # BING IMG
import textsurfer
import random
#############################################

# MICROSOFT TRANSLATE API
microsoft_id = 'patalator'
microsoft_secret = 'IXfoWZgfMnQ6JFe9UmWcbGxoum+kr6DwFefNh1bFhcM='

# FLICKR API
api_key = '9a9ab31b6a0003ab43b64088230eb120'

# BING IMAGE SEARCH API
# username fania@web.de pw = key
key = 'KxnH3+uL1TGRJkGlQ5gg7Dwri6GfV121ezf27TRbvUY='


def pataphysicalise(words):
    sys_ws = []
    for word in words:
        _, w, _, _ = textsurfer.syzygy(word)
        sys_ws.append(w)
    sres = []
    for s in sys_ws:
        sres.append((random.sample(s, 1))[0])
    t = ' '.join(sres)
    translations = transent(t)
    return translations


def transent(sent):
    translator = Translator(microsoft_id, microsoft_secret)
    french = translator.translate(sent, "fr")
    japanese = translator.translate(french, "ja")
    patawords = translator.translate(japanese, "en")
    translations = (french, japanese, patawords)
    return translations


def getimages(query):
    # print('inside getImages query', query)
    out = []
    words = query.split()

    translations = pataphysicalise(words)
    patawords = translations[2]
    # print('patawords', patawords)

    # # FLICKR
    # flickr = flickrapi.FlickrAPI(api_key)
    # if flickr:
    #     print('flickr', flickr)
    # else:
    #     print('error')
    # photos = flickr.photos_search(text=patawords, per_page='10',
    #                               safe_search='1')
    #
    # # owners = set()
    # for photo in photos[0]:
    #     photoid = photo.attrib['id']
    #     phototitle = photo.attrib['title']
    #     photoowner = photo.attrib['owner']
    #     photoSizes = flickr.photos_getSizes(photo_id=photoid)
    #     photothumb = photoSizes[0][1].attrib['source']
    #     photolink = "http://www.flickr.com/photos/%s/%s" % \
    #                 (photoowner, photoid)
    #     # if photoowner not in owners and len(owners) < 10:
    #     #     owners.add(photoowner)
    #     out.append((phototitle, photothumb, photolink))

    # BING IMAGES
    base = "https://api.datamarket.azure.com/Bing/Search/"
    params = "Image?$format=json&Query='%s'" % patawords
    url = ''.join([base, params])
    bing_img = requests.get(url, auth=HTTPBasicAuth(None, key))
    for result in bing_img.json()['d']['results']:
        phototitle = result['Title']
        photoimg = result['MediaUrl']
        photolink = result['SourceUrl']
        out.append((phototitle, photoimg, photolink))

    return out, translations
