from __future__ import print_function
from flask import url_for
from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader
import os
import nltk
import codecs
import sys
import warnings

#import unicodedata as ud

#print sys.getdefaultencoding()
# Ignore weird unicode warnings from dameraulevenshtein function
# warnings.simplefilter('ignore')

#############################################

# PROTOTYPE 01 - TEXT

#############################################

root_path = os.path.dirname(os.path.abspath(__file__))
#print 'root_path ', root_path
#corpus_root = os.path.join(root_path, 'corpus')
#root_path = root_path[:-11]
root_path = root_path[:-4]
#root_path = 'G:\Code\\newpata\\'
#corpus_root = os.path.join(root_path, 'corpus')
corpus_root = root_path + '/app/static/corpus'

# NLTK way to import txt into a list #######################
book_list = PlaintextCorpusReader(corpus_root, '.*\.txt')
#book_list = PlaintextCorpusReader(corpus_root, '[A-z]*\.txt')
#print book_list
troll = book_list.words('faustroll.txt')
faustroll = nltk.Text(troll)
############################################################

############################################################

for ct in book_list.fileids():
    print('ID:', ct)
    print(' '.join(book_list.words(ct)[0:10]))
    # num_chars = len(book_list.raw(ct))
    # print('num_chars', num_chars)
    # num_words = len(book_list.words(ct))
    # print('num_words', num_words)
    # # print(book_list.sents(ct)[0:5])
    # # num_sents1 = len(book_list.sents(ct))
    # # print('num_sents1', num_sents1)
    # num_vocab = len(set(w.lower() for w in book_list.words(ct)))
    # print('num_vocab', num_vocab)
    # print(round(num_chars/num_words), round(num_words/num_vocab))


# bloycode = [i.encode('utf-8') for i in bloytext]
# bloy1 = bloycode
# print('++++++++++++++++++++')
# print('bloy1:')
# print(bloy1[0:100])

# UNICODE TESTS

# Fania's Non-NLTK way to import txt file
#path_f = os.path.join(root_path, 'corpus/faustroll.txt')
#faustroll_text = open(path_f, "r")
#text = [i.lower() for line in faustroll_text.readlines() for i in line.split()]
#faustroll_text.close()
#faustroll = text

from nltk.corpus import stopwords
en_stop = stopwords.words('english')
fr_stop = stopwords.words('french')
de_stop = stopwords.words('german')
# print(en_stop)
# print(de_stop)
# print(fr_stop)

path_e = corpus_root + '/english'
stopwords_doc = open(path_e, "r")
sw = [i for line in stopwords_doc.readlines() for i in line.split()]
stopwords_doc.close()
# print(sw)
faustroll_dict = sorted(set([w.lower() for w in faustroll]))
froll_dict = [w for w in faustroll_dict if w.isalpha() and w not in sw]
# ud.normalize('NFKD', w).encode('ascii', 'ignore')


word_freq1 = nltk.FreqDist(faustroll)
print(word_freq1['Faustroll'])
print(word_freq1.pprint())



#
# for fileid in book_list.fileids():
#     num_chars = len(book_list.raw(fileid))
#     num_words = len(book_list.words(fileid))
#     num_sents1 = len(book_list.sents(fileid))
#     num_vocab = len(set(w.lower() for w in book_list.words(fileid)))
#     print(round(num_chars/num_words), round(num_words/num_sents1), round(num_words/num_vocab), fileid)
    # print(round(num_chars/num_words))
    # print(round(num_words/num_sents1))
    # print(round(num_words/num_vocab))
    # print(fileid)










# print('book_list:')
# print(book_list)
# print(book_list.fileids())
# print('------------------------\n')
# print('troll:')
# print(troll)
# print(book_list.sents('faustroll.txt')[1:10])
# print('------------------------\n')
# print('faustroll:')
# print(faustroll)
# print('\n')
# print('faustroll.collocations:')
# print(faustroll.collocations())
# print('\n')
# print('faustroll.concordance.Faustroll:')
# print(faustroll.concordance('Faustroll'))
# print('\n')
# print('faustroll.count.he:')
# print(faustroll.count('he'))
# print('\n')
# # print(faustroll.dispersion_plot(['I','Faustroll','He He']))
# print('faustroll.vocab:')
# print(faustroll.vocab())
# print('faustroll.fdist.Faustroll:')
# fdist = nltk.FreqDist(faustroll)
# modals = ['Faustroll', 'speak', 'year', 'skiff', 'FAUSTROLL']
# for m in modals:
#     print(m + ':',fdist[m], end=' ')
# print('\n')
# print('------------------------\n')
# print('faustroll_dict:')
# print(faustroll_dict[1:100])
# print('------------------------\n')
# print('froll_dict:')
# print(froll_dict[1:100])
# print('------------------------\n')
# print('sw:')
# print(sw)
# print('------------------------\n')


# import itertools
# fdist_most_common = fdist.most_common()
# # print(fdist_most_common)
#
# list_most_common = list(itertools.chain(*(sorted(ys) for k, ys in itertools.groupby(fdist_most_common, key=lambda t: t[1]))))
#
# print(list_most_common[1:100])
# print('------------------------\n')





def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)


def syzygy(word):
    out = set()
    wordsets = wn.synsets(word)  # returns a list of synsets
    for w in wordsets:  # w is a synset
        # Hyponyms share a type-of relationship with their hypernym
        hypo = w.hyponyms()  # returns a list of synsets
        if len(hypo) > 0:
            for h in hypo:  # h is a synset
                for l in h.lemmas():  # l is a lemma
                    if str(l.name()) in froll_dict:
                        out.add(str(l.name()))
        # Hyponyms share a type-of relationship with their hypernym
        hyper = w.hypernyms()
        if len(hyper) > 0:
            for h in hyper:
                for l in h.lemmas():
                    if str(l.name()) in froll_dict:
                        out.add(str(l.name()))
        # 'X' is a holonym of 'Y' if Ys are parts of Xs, or
        # 'X' is a holonym of 'Y' if Ys are members of Xs.
        holo = w.member_holonyms()
        if len(holo) > 0:
            for h in holo:
                for l in h.lemmas():
                    if str(l.name()) in froll_dict:
                        out.add(str(l.name()))
    return out

# print('SYZYGY')
# synwords = wn.synsets('clear')
# print('synsets:')
# print(synwords)
# for w in synwords:
#     # print('synset item:' + str(w.name()))
#     hypo = w.hyponyms()
#     if len(hypo) > 0:
#         for h in hypo:
#             for l in h.lemmas():
#                 # print('hyponym out:' + str(l.name()))
#                 if str(l.name()) in froll_dict:
#                     # print('hyponym in:' + str(l.name()))
#     hyper = w.hypernyms()
#     if len(hyper) > 0:
#         for h in hyper:
#             for l in h.lemmas():
#                 # print('hypernym out:' + str(l.name()))
#                 if str(l.name()) in froll_dict:
#                     # print('hypernym in:' + str(l.name()))
#     holo = w.member_holonyms()
#     print(holo)
#     if len(holo) > 0:
#         for h in holo:
#             for l in h.lemmas():
#                 # print('holonym out:' + str(l.name()))
#                 if str(l.name()) in froll_dict:
#                     # print('holonym in:' + str(l.name()))
#


def antinomy(word):
    out = set()
    wordsets = wn.synsets(word)
    for w in wordsets:
        anti = w.lemmas()[0].antonyms()
        if len(anti) > 0:
            for a in anti:
                if str(a.name()) != word:
                    out.add(str(a.name()))
    return out


# print('ANTINOMY')
# antwords = wn.synsets('clear')
# print('synsets:')
# print(antwords)
# for w in antwords:
#     # print('synset item:' + str(w.name()))
#     anti = w.lemmas()[0].antonyms()
#     if len(anti) > 0:
#         for a in anti:
#             # print('antonym out:' + str(a.name()))
#             if str(a.name()) != 'clear':
#                 # print('antonym in:' + str(a.name()))
#


def find_sentence(word):
    out = []
    if faustroll.count(word) > 0:
        # indices = [i for i, x in enumerate(faustroll) if x == word]
        pos = faustroll.index(word)
        pos_b = pos - 5
        pos_a = pos + 5
        if pos_b >= 0 and pos_a <= len(faustroll):
            out = (' '.join(faustroll[pos_b:pos]), ' '.join(faustroll[pos:pos_a]))
    return out


def pre_sentence(word):
    out = []
    if faustroll.count(word) > 0:
        pos = faustroll.index(word)
        pos_b = pos - 5
        if pos_b >= 0:
            out = ' '.join(faustroll[pos_b:pos])
    return out


def post_sentence(word):
    out = []
    if faustroll.count(word) > 0:
        pos = faustroll.index(word) + 1
        pos_a = pos + 5
        if pos_a <= len(faustroll):
            out = ' '.join(faustroll[pos:pos_a])
    return out


def clinamen(word, i):
    out = set()
    items = [item for item in froll_dict if dameraulevenshtein(word, item) <= i]
    for item in items:
        if item != word:
            out.add(item)
    return out


# Taken from http://mwh.geek.nz/2009/04/26/python-damerau-levenshtein-distance/
# MIT license.
def dameraulevenshtein(seq1, seq2):
    oneago = None
    thisrow = range(1, len(seq2) + 1) + [0]
    for x in xrange(len(seq1)):
        # Python lists wrap around for negative indices, so put the
        # leftmost column at the *end* of the list. This matches with
        # the zero-indexed strings and saves extra calculation.
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in xrange(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
            # This block deals with transpositions
            if (x > 0 and y > 0 and seq1[x] == seq2[y - 1]
                    and seq1[x - 1] == seq2[y] and seq1[x] != seq2[y]):
                thisrow[y] = min(thisrow[y], twoago[y - 2] + 1)
    return thisrow[len(seq2) - 1]


############################
# Fania's Non-NLTK way to import txt file
#root_path = os.path.dirname(os.path.realpath(__file__))
#path_f = os.path.join(root_path, 'corpus/faustroll.txt')
#faustroll_text = open(path_f, "r")
#text = [i.lower() for line in faustroll_text.readlines() for i in line.split()]
#faustroll_text.close()
#faustroll = text
#path_e = os.path.join(root_path, 'corpus/english')
#stopwords_doc = open(path_e, "r")
#sw = [i for line in stopwords_doc.readlines() for i in line.split()]
#stopwords_doc.close()

# def get_concordances(word):
#    return faustroll.concordance(word)
# print(get_concordances('skiff'))
