from microsofttranslator import Translator
import flickrapi as fapi
import json
# from getty import Session
import requests  # BING IMG
# import urllib
# import urllib2
# import urllib
from requests.auth import HTTPBasicAuth  # BING IMG
from textsurfer import syzygy
import itertools
#############################################

# MICROSOFT TRANSLATE API
# microsoft_id = 'patalator'
# microsoft_secret = 'IXfoWZgfMnQ6JFe9UmWcbGxoum+kr6DwFefNh1bFhcM='

# FLICKR API
# application = 'plickr'
# flickr_key = u'9a9ab31b6a0003ab43b64088230eb120'
# flickr_secret = u'16f11edd3d9d0cec'

# BING IMAGE SEARCH API
# username fania@web.de pw = key
# bing_key = 'KxnH3+uL1TGRJkGlQ5gg7Dwri6GfV121ezf27TRbvUY='

# GETTY API
# GET  https://api.gettyimages.com/v3/search/
# images?fields=id,title,thumb,referral_destinations&sort_order=best&
# phrase=pataphysics
#
# faniiia
# Connect Embed
# Application: PataSearch
# getty_key = '992thepbk9a25nu7sefeqncz'
# getty_secret = 'FqWekE4BfRhB3A2VtufzUgbTVRknXqqhxaVGp7FdQ9T8E'


def pataphysicalise(words):
    sys_ws = []
    for word in words:
        _, w, _, _ = syzygy(word)
        if len(w) > 0:
            sys_ws.append(list(w))
    out = itertools.product(*sys_ws)
    return list(out)


def transent(sent):
    microsoft_id = 'patalator'
    microsoft_secret = 'IXfoWZgfMnQ6JFe9UmWcbGxoum+kr6DwFefNh1bFhcM='
    translator = Translator(microsoft_id, microsoft_secret)
    french = translator.translate(sent, "fr")
    japanese = translator.translate(french, "ja")
    patawords = translator.translate(japanese, "en")
    translations = (french, japanese, patawords)
    return translations


def getimages(query, choice):
    words = query.split()
    tmp = pataphysicalise(words)
    if choice == 'Bing':
        return get_Bing(tmp)
    if choice == 'Flickr':
        return get_Flickr(tmp)
    if choice == 'Google':
        return get_Google(tmp)
    if choice == 'Getty':
        return get_Getty(tmp)


def get_Bing(words):
    out = []
    trans = ''
    bing_key = 'KxnH3+uL1TGRJkGlQ5gg7Dwri6GfV121ezf27TRbvUY='
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


def get_Flickr(words):
    out = []
    trans = ('', '', '')
    flickr_key = u'9a9ab31b6a0003ab43b64088230eb120'
    flickr_secret = u'16f11edd3d9d0cec'
    # base = "https://api.flickr.com/services/rest/"
    # params0 = "?method=flickr.photos.search"
    # params1 = "&api_key=9a9ab31b6a0003ab43b64088230eb120&text="
    # params2 = "&safe_search=1&format=json&nojsoncallback=1"
    for x in words:
        y = ' '.join(x)
        z = transent(y)
        trans = z
        flickr = fapi.FlickrAPI(flickr_key, flickr_secret, format='json')
        fotos = flickr.photos.search(text=z[2], per_page='10', safe_search=1)
        parsed = json.loads(fotos.decode('utf-8'))
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
            break
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
