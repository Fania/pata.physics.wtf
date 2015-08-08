from flask import Flask

import random
import os
import codecs

application = Flask(__name__)



def getrandquote():
    # RANDOM QUOTES
    root_path = os.path.dirname(os.path.abspath(__file__))
    root_path = root_path[:-4]
    corpus_root = root_path + '/app/static/corpus'
    path_b = corpus_root + '/quotes.txt'
    quotes_text = codecs.open(path_b, "r", encoding='utf-8')
    quotestext = quotes_text.readlines()
    quotes_text.close()
    # print random.choice(quotestext)
    return random.choice(quotestext)

application.jinja_env.globals.update(getrandquote=getrandquote)

from app import views
