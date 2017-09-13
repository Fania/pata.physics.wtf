from flask import Flask
import random
import os
import codecs

app = Flask(__name__)

from app import views, textviews, imageviews, videoviews, audioviews


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

app.jinja_env.globals.update(getrandquote=getrandquote)
