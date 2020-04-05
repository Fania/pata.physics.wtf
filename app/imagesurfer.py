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




def getFlickrImages(queries, choice):
  # output = queries + [choice]
  tags = ",".join(queries)
  print(tags)
  endpoint = 'https://www.flickr.com/services/feeds/photos_public.gne'
  params = '?format=json&jsoncallback&tagsmode=any&tags='
  # headers = {
  #   'api_key': flickr_k
  # }

  fullUrl = endpoint + params + tags
  responseJson = requests.post(fullUrl)
  # response = json.dumps(responseJson)
  # response = responseJson.json()
  response = responseJson.text
  print(responseJson)
  print(response)
  # print(response)


  return responseJson



# // FLICKR
# function flickrsearch(queries){
#   console.log("flickr");
#   let results = [];
#   const tags = queries.join(",");
#   const baseURL = `https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=${keyconfig.flickr_k}&format=json&per_page=10&nojsoncallback=1&sort=date-taken-desc&safe_search=1&tags=`;
#   const url = baseURL + tags;
#   const request = new Request(url);
#   fetch(request)
#     .then(response => response.json())
#     .then(data => {
#       (data.photos.photo).forEach(d => {
#         if (d != undefined) {
#           const img_url = `https://farm${d.farm}.staticflickr.com/${d.server}/${d.id}_${d.secret}_q.jpg`;
#           const page_url = `https://www.flickr.com/photos/${d.owner}/${d.id}`;
#           results.push([d.title, img_url, page_url]);
#         }
#       });
#       createSpiral(results);
#     });
# }; // end flickrsearch