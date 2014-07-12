from flask import Flask
import random, os
import unicodedata, codecs


app = Flask(__name__)

from app import views, views01, views02, views03


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
