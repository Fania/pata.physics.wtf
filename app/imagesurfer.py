import json
import requests
import itertools
from nltk.corpus import wordnet as wn
from .keys import *

def pataphysicalise(words):
    # print('inside pata: query words: ', words)
    sys_ws = set()
    for word in words:
        # print(word)
        synonyms = wn.synsets(word)
        # print(word, synonyms)
        if len(synonyms) > 0:
            for s in synonyms:
                for l in s.lemmas():
                    x = str(l.name())
                    # print(x)
                    o = x.replace('_', ' ')
                    sys_ws.add(o)
    # print('synonyms ', sys_ws)
    return sys_ws

# print(pataphysicalise('fluffy cats'))


def transent(sent):
    # Call to Microsoft Translator Service

    # https://docs.microsoft.com/en-gb/azure/cognitive-services/translator/reference/v3-0-reference
    # see also https://github.com/MicrosoftTranslator/Text-Translation-API-V3-Python/blob/master/Translate.py

    # print("Inside translator function: ", sent)

    endpoint = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'
    headers = {
      'Ocp-Apim-Subscription-Key': translator_s,
      'Content-type': 'application/json'
    }

    frbody = [{'text': sent}]
    frurl = endpoint + "&from=en&to=fr"
    frtranslationData = requests.post(frurl, headers=headers, json=frbody)
    frresponse = frtranslationData.json()
    french = frresponse[0]['translations'][0]['text']
    # print(french)

    jabody = [{'text': french}]
    jaurl = endpoint + "&from=fr&to=ja"
    jatranslationData = requests.post(jaurl, headers=headers, json=jabody)
    jaresponse = jatranslationData.json()
    japanese = jaresponse[0]['translations'][0]['text']
    # print(japanese)

    enbody = [{'text': japanese}]
    enurl = endpoint + "&from=ja&to=en"
    entranslationData = requests.post(enurl, headers=headers, json=enbody)
    enresponse = entranslationData.json()
    english = enresponse[0]['translations'][0]['text']
    # print(english)

    translations = (french, japanese, english)
    return translations




def getFlickrImages(queries):
  tags = ",".join(queries)
  endpoint = f'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={flickr_k}&format=json&per_page=10&nojsoncallback=1&sort=date-taken-desc&safe_search=1&tags={tags}'
  responseJson = requests.post(endpoint)
  response = responseJson.json()
  output = []
  for item in response['photos']['photo']:
    imgUrl = f'https://farm{item["farm"]}.staticflickr.com/{item["server"]}/{item["id"]}_{item["secret"]}_q.jpg'
    url = f'https://www.flickr.com/photos/{item["owner"]}/{item["id"]}'
    op = [item['title'], imgUrl, url]
    output.append(op)
  return output





def getBingImages(queries):
  queryString = " | ".join(queries)
  endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
  headers = { "Ocp-Apim-Subscription-Key": bing_k }
  params = { "q": queryString, "count": 10 }
  response = requests.get(endpoint, headers=headers, params=params)
  response.raise_for_status()
  search_results = response.json()
  output = []
  for item in search_results['value']:
    op = [item['name'], item['thumbnailUrl'], item['hostPageUrl']]
    output.append(op)
  return output
