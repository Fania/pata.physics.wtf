from microsofttranslator import Translator
import flickrapi as fapi
import json
import requests  # BING IMG
from requests.auth import HTTPBasicAuth  # BING IMG
import itertools
from nltk.corpus import wordnet as wn
import keys
from auth import AzureAuthClient  # Translator
from xml.etree import ElementTree  # Translator

# from textsurfer import syzygy
import itertools
from nltk.corpus import wordnet as wn

import sys

reload(sys)  
sys.setdefaultencoding('utf8')


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


def transent(sent):
    # Call to Microsoft Translator Service

    client_secret = keys.translator_s
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
