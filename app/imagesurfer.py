from microsofttranslator import Translator
import flickrapi as fapi
import json
# from getty import Session
import requests  # BING IMG
# import urllib
# import urllib2
# import urllib
from requests.auth import HTTPBasicAuth  # BING IMG
from auth import AzureAuthClient  # Translator
from xml.etree import ElementTree  # Translator

# from textsurfer import syzygy
import itertools
from nltk.corpus import wordnet as wn


import sys

reload(sys)  
sys.setdefaultencoding('utf8')
#############################################

# MICROSOFT TRANSLATE API
# microsoft_id = 'patalator'
# microsoft_secret = 'IXfoWZgfMnQ6JFe9UmWcbGxoum+kr6DwFefNh1bFhcM='
# new details
# key 1 = 'c1e02f3572ad4280bef1fce290a7323f'



# FLICKR API
# application = 'plickr'
# flickr_key = u'9a9ab31b6a0003ab43b64088230eb120'
# flickr_secret = u'16f11edd3d9d0cec'

# BING IMAGE SEARCH API
# username fania@web.de pw = key
# bing_key = 'UC5GBf1nozBOxJImxv9HS9Qb1aNzXuWDCPDy5D/4NlY='


# GETTY API
# GET  https://api.gettyimages.com/v3/search/
# images?fields=id,title,thumb,referral_destinations&sort_order=best&
# phrase=pataphysics
# faniiia
# Connect Embed
# Application: PataSearch
# getty_key = '992thepbk9a25nu7sefeqncz'
# getty_secret = 'FqWekE4BfRhB3A2VtufzUgbTVRknXqqhxaVGp7FdQ9T8E'


# def syzygy(w, c):
#     words = set()
#     wordsets = wn.synsets(w)
#     for ws in wordsets:
#         words.update(get_nym('hypo', ws))
#         words.update(get_nym('hyper', ws))
#         words.update(get_nym('holo', ws))
#     print('inside syzygy function: ', words)
#     out, sources, total = get_results(words, 'Syzygy', c)
#     return out, words, sources, total

# for l in h.lemmas():
#                 out.append(str(l.name()))


def pataphysicalise(words):
    # print('inside pata: query words: ', words)
    sys_ws = set()
    for word in words:
        synonyms = wn.synsets(word)
        if len(synonyms) > 0:
            for s in synonyms:
                for l in s.lemmas():
                    x = str(l.name())
                    o = x.replace('_', ' ')
                    sys_ws.add(o)
    # print('synonyms ', sys_ws)
    return sys_ws

# print(pataphysicalise('fluffy cats'))


# def transent(sent):
#     microsoft_id = 'patalator'
#     microsoft_secret = 'IXfoWZgfMnQ6JFe9UmWcbGxoum+kr6DwFefNh1bFhcM='
#     translator = Translator(microsoft_id, microsoft_secret)
#     french = translator.translate(sent, "fr")
#     japanese = translator.translate(french, "ja")
#     patawords = translator.translate(japanese, "en")
#     translations = (french, japanese, patawords)
#     return translations


def transent2(sent):
    # Call to Microsoft Translator Service

    client_secret = 'c1e02f3572ad4280bef1fce290a7323f'
    auth_client = AzureAuthClient(client_secret)
    bearer_token = 'Bearer ' + auth_client.get_access_token()
    headers = {"Authorization ": bearer_token}

    frurl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&from={}&to={}".format(sent, 'en', 'fr')
    frtranslationData = requests.get(frurl, headers = headers)
    frtranslation = ElementTree.fromstring(frtranslationData.text.encode('utf-8'))
    french = frtranslation.text.encode('utf-8')

    japurl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&from={}&to={}".format(french, 'fr', 'ja')
    jatranslationData = requests.get(japurl, headers = headers)
    jatranslation = ElementTree.fromstring(jatranslationData.text.encode('utf-8'))
    japanese = jatranslation.text.encode('utf-8')

    engurl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&from={}&to={}".format(japanese, 'ja', 'en')
    entranslationData = requests.get(engurl, headers = headers)
    entranslation = ElementTree.fromstring(entranslationData.text.encode('utf-8'))
    english = entranslation.text.encode('utf-8')

    translations = (french, japanese, english)
    return translations



##################################################
#          NOT USED AT THE MOMENT                #
################################################## 


def getimages(pata, choice):
    for query in pata:
        if choice == 'flickr':
            return get_Flickr(query)
        # if choice == 'bing':
        #     return get_Bing(query)
        if choice == 'getty':
            return get_Getty(query)
        # if choice == 'google':
        #     return get_Google(tmp)


def get_Flickr(words):
    print('started flickr function')
    out = []
    trans = ('', '', '')
    flickr_key = u'9a9ab31b6a0003ab43b64088230eb120'
    flickr_secret = u'16f11edd3d9d0cec'
    # base = "https://api.flickr.com/services/rest/"
    # params0 = "?method=flickr.photos.search"
    # params1 = "&api_key=9a9ab31b6a0003ab43b64088230eb120&text="
    # params2 = "&safe_search=1&format=json&nojsoncallback=1"
    for x in words:
        print('begin loop')
        y = ' '.join(x)
        z = transent(y)
        trans = z
        flickr = fapi.FlickrAPI(flickr_key, flickr_secret, format='json')
        fotos = flickr.photos.search(text=z[2], per_page='10', safe_search=1)
        parsed = json.loads(fotos.decode('utf-8'))
        print(parsed)
        if parsed['photos']['total'] >= 10:
            for p in parsed['photos']['photo']:
                pid = p['id']
                ptitle = p['title']
                powner = p['owner']
                # psecret = p['secret']
                # pserver = p['server']
                # pfarm = p['farm']
                psizes = flickr.photos.getSizes(photo_id=pid, format='json')
                parsize = json.loads(psizes.decode('utf-8'))
                pthumb = parsize['sizes']['size'][1]['source']
                plink = "http://www.flickr.com/photos/%s/%s" % \
                        (powner, pid)
                # plink1 = "https://farm%s.staticflickr.com/" % pfarm
                # plink2 = "%s/" % pserver
                out.append((ptitle, pthumb, plink))
                print('added result')
            break
    print('end flickr function')
    return out, trans
    

def get_Bing(words):
    out = []
    trans = ''
    bing_key = 'UC5GBf1nozBOxJImxv9HS9Qb1aNzXuWDCPDy5D/4NlY='
    base = "https://api.datamarket.azure.com/Bing/Search/"
    params = "Image?$format=json&Query='"
    after = "'"
    for x in words:
        y = ' '.join(x)
        z = transent(y)
        url = ''.join([base, params, z[2], after])
        bing_img = requests.get(url, auth=HTTPBasicAuth(None, bing_key))
        if bing_img.json()['d']['results']:
            trans = z
            for result in bing_img.json()['d']['results']:
                phototitle = result['Title']
                photoimg = result['MediaUrl']
                photolink = result['SourceUrl']
                out.append((phototitle, photoimg, photolink))
            break
        else:
            out = []
    return out, trans


def get_Google(words):
    print('google')
    return [], ('', '', '')


def get_Getty(words):
    getty_key = '5kt5jxty5vvb8zxev3yzd4dz'
    # getty_secret = 'CvwGwqvuKBWQn8bqctcQ5TCaujd8Ux3VPJsGgZ2zkPqkV'
    print('getty')
    out = []
    trans = ''
    base = "https://api.gettyimages.com/v3/search/images/creative?"
    params = "exclude_nudity=true&license_models=royaltyfree&phrase='"
    after = "'"
    headers = {'Api-Key': getty_key}
    for x in words:
        y = ' '.join(x)
        z = transent(y)
        print('pataword', z[2])
        rurl = ''.join([base, params, z[2], after])
        r = requests.get(rurl, headers=headers)
        rj = r.json()
        if rj['result_count'] >= 10:
            trans = z
            print('sucess')
            for result in rj['images']:
                ptitle = result['title']
                print(ptitle)
                pimg = result['display_sizes'][0]['uri']
                print(pimg)
                plink = pimg
                out.append((ptitle, pimg, plink))
            break
        else:
            out = []
    return out, trans
