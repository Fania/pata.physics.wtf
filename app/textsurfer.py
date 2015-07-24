
from __future__ import print_function
# from flask import url_for
from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

# from operator import indexOf
from collections import defaultdict

import os
import nltk
# import codecs
import sys
# import warnings

# import unicodedata as ud

# print sys.getdefaultencoding()
# Ignore weird unicode warnings from dameraulevenshtein function
# warnings.simplefilter('ignore')

#############################################

# PROTOTYPE 01 - TEXT

#############################################

root_path = os.path.dirname(os.path.abspath(__file__))
# print 'root_path ', root_path
# corpus_root = os.path.join(root_path, 'corpus')
# root_path = root_path[:-11]
root_path = root_path[:-4]
# root_path = 'G:\Code\\newpata\\'
# corpus_root = os.path.join(root_path, 'corpus')
corpus_root = root_path + '/app/static/corpus'

# NLTK way to import txt into a list #######################
book_list = PlaintextCorpusReader(corpus_root, '.*\.txt')  # root, fileid
# book_list = PlaintextCorpusReader(corpus_root, '[A-z]*\.txt')
# print book_list
troll = book_list.words('00.faustroll.txt')
faustroll = nltk.Text(troll)

############################################################
l_00 = book_list.words('00.faustroll.txt')
l_01 = book_list.words('01.poe1.txt')
# l_01 = book_list.words('01.poe2.txt')
# l_01 = book_list.words('01.poe3.txt')
# l_01 = book_list.words('01.poe4.txt')
# l_01 = book_list.words('01.poe5.txt')
l_02 = book_list.words('02.bergerac.txt')
l_03 = book_list.words('03.gospel.txt')
l_04 = book_list.words('04.bloy_french.txt')
l_05 = book_list.words('05.coleridge.txt')
l_06 = book_list.words('06.darien_french.txt')
l_07 = ''
l_08 = book_list.words('08.elskamp_french.txt')
l_09 = book_list.words('09.florian_french.txt')
l_10 = book_list.words('10.arabiannights.txt')
l_11 = book_list.words('11.grabbe_german.txt')
l_12 = book_list.words('12.kahn_french.txt')
l_13 = book_list.words('13.lautreamont_french.txt')
l_14 = book_list.words('14.maeterlinck.txt')
l_15 = book_list.words('15.mallarme_french.txt')
l_16 = ''
l_17 = book_list.words('17.odyssey.txt')
l_18 = ''
l_19 = book_list.words('19.rabelais.txt')
l_20 = ''
l_21 = ''
l_22 = book_list.words('22.rimbaud_french.txt')
l_23 = book_list.words('23.schwob_german.txt')
l_24 = book_list.words('24.ubu_french.txt')
l_25 = book_list.words('25.verlaine.txt')
l_26 = book_list.words('26.verhaeren.txt')
l_27 = book_list.words('27.verne.txt')
############################################################
en_stop = stopwords.words('english')  # print(en_stop)
fr_stop = stopwords.words('french')  # print(fr_stop)
de_stop = stopwords.words('german')  # print(de_stop)
############################################################

l_dict = defaultdict(list)
# print('l_dict before')
# print(l_dict.items())


def setupcorpus(nr, lang):
    # ll = [w.lower() for w in nr if w.isalpha() and w.lower() not in lang]
    for x, w in enumerate(nr):
        # print(w)
        # x = indexOf(nr, w)
        if w.isalpha() and (w.lower() not in lang):
            l_dict[w.lower()].append([nr.fileid[49:], x])
            # l_dict[w.lower()].append([nr.fileid[49:], nr.index(w)])


# def testindex(nr, w):
#     print('testing', w, nr)
#     if w in nr:
#         print(nr.index(w))
#     else:
#         print('error')
#
#
# testindex(l_01, 'fawn')
# testindex(l_01, 'Fawn')
# testindex(l_01, 'FAWN')
# testindex(l_17, 'fawn')
# testindex(l_17, 'Fawn')
# testindex(l_17, 'FAWN')
# testindex(l_19, 'fawn')
# testindex(l_19, 'Fawn')
# testindex(l_19, 'FAWN')
# print(l_dict['fawn'])

# print('54140', l_01.index('fawn'))
# print('54140', l_01.index('Fawn'))
# print('111976', l_17.index('fawn'))
# print('111976', l_17.index('Fawn'))


# for w in sorted(set(ll)):
#     # l_dict[w].append((nr.fileid[49:], ll.count(w)))  # SLOW
#     # l_dict[w].append([nr.fileid[49:], 0])
#     if w in nr:
#         l_dict[w].append([nr.fileid[49:], nr.index(w)])
#     else:
#         # if w.capitalize() in nr:
#         l_dict[w].append([nr.fileid[49:], nr.index(w.capitalize())])
# pass

# corpus_list = [l_00, l_01, l_02, l_03, l_04, l_05, l_06, l_07, l_08,
#                l_09, l_10, l_11, l_12, l_13, l_14, l_15, l_16, l_17,
#                l_18, l_19, l_20, l_21, l_22, l_23, l_24, l_25, l_26,
#                l_27]

# l_dict structure:
# {word1: [[fileA, 0], [fileB, 0], ...],
#  word2: [[fileC, 0], [fileK, 0], ...],
#  ...
# }


# def completecorpus():
#     # for cnt, k in enumerate(l_dict.keys()):  # word1
#     for k in l_dict.keys():  # word1
#         # print(cnt, '/', len(l_dict), k)
#         for f in l_dict[k]:  # (fileK, 0)
#             x = 'l_' + (f[0])[0:2]
#             if k in eval(x):
#                 f[1] = eval(x).index(k)
#             else:
#                 if k.capitalize() in eval(x):
#                     f[1] = eval(x).index(k.capitalize())


setupcorpus(l_00, en_stop), print('added 00')
setupcorpus(l_01, en_stop), print('added 01')
setupcorpus(l_02, en_stop), print('added 02')
setupcorpus(l_03, en_stop), print('added 03')
setupcorpus(l_04, fr_stop), print('added 04')
setupcorpus(l_05, en_stop), print('added 05')
setupcorpus(l_06, fr_stop), print('added 06')
setupcorpus(l_07, en_stop), print('added 07')
setupcorpus(l_08, fr_stop), print('added 08')
setupcorpus(l_09, fr_stop), print('added 09')
setupcorpus(l_10, en_stop), print('added 10')
setupcorpus(l_11, en_stop), print('added 11')
setupcorpus(l_12, fr_stop), print('added 12')
setupcorpus(l_13, fr_stop), print('added 13')
setupcorpus(l_14, en_stop), print('added 14')
setupcorpus(l_15, fr_stop), print('added 15')
setupcorpus(l_16, en_stop), print('added 16')
setupcorpus(l_17, en_stop), print('added 17')
setupcorpus(l_18, en_stop), print('added 18')
setupcorpus(l_19, en_stop), print('added 19')
setupcorpus(l_20, en_stop), print('added 20')
setupcorpus(l_21, en_stop), print('added 21')
setupcorpus(l_22, fr_stop), print('added 22')
setupcorpus(l_23, de_stop), print('added 23')
setupcorpus(l_24, fr_stop), print('added 24')
setupcorpus(l_25, en_stop), print('added 25')
setupcorpus(l_26, en_stop), print('added 26')
setupcorpus(l_27, en_stop), print('added 27')
print('l_dict after')
# print((l_dict.items())[0:20])
# print(l_dict['fawn'])


# print('completing corpus:')
# completecorpus()

# print('complete l_dict')
# print((l_dict.items())[0:20])

# ---------------------------------------------
#
# faustroll_dict = sorted(set([w.lower() for w in faustroll]))
# froll_dict = [w for w in faustroll_dict if w.isalpha() and w not in en_stop]
# ud.normalize('NFKD', w).encode('ascii', 'ignore')

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


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)


# def syzygy(word):
#     out = set()
#     wordsets = wn.synsets(word)  # returns a list of synsets
#     for w in wordsets:  # w is a synset
#         # Hyponyms share a type-of relationship with their hypernym
#         hypo = w.hyponyms()  # returns a list of synsets
#         if len(hypo) > 0:
#             for h in hypo:  # h is a synset
#                 for l in h.lemmas():  # l is a lemma
#                     if str(l.name()) in froll_dict:
#                         out.add(str(l.name()))
#         # Hyponyms share a type-of relationship with their hypernym
#         hyper = w.hypernyms()
#         if len(hyper) > 0:
#             for h in hyper:
#                 for l in h.lemmas():
#                     if str(l.name()) in froll_dict:
#                         out.add(str(l.name()))
#         # 'X' is a holonym of 'Y' if Ys are parts of Xs, or
#         # 'X' is a holonym of 'Y' if Ys are members of Xs.
#         holo = w.member_holonyms()
#         if len(holo) > 0:
#             for h in holo:
#                 for l in h.lemmas():
#                     if str(l.name()) in froll_dict:
#                         out.add(str(l.name()))
#     return out

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


# def antinomy(word):
#     out = set()
#     wordsets = wn.synsets(word)
#     for w in wordsets:
#         anti = w.lemmas()[0].antonyms()
#         if len(anti) > 0:
#             for a in anti:
#                 if str(a.name()) != word:
#                     out.add(str(a.name()))
#     return out


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


# def fullsent(w, f):
#     out = []
#     ff = eval(f)
#     pos = 0
#     if ff.count(w) > 0:
#         pos = ff.index(w)
#     else:
#         pos = ff.index(w.capitalize())
#     pos_b = pos - 5
#     pos_a = pos + 5
#     if pos_b >= 0 and pos_a <= len(ff):
#         out = ' '.join(ff[pos_b:pos_a])
#     # print('sentences')
#     # print(out)
#     return out
# print(fullsent('clear', 'l_00'))


def pp_sent(w, f):
    out = []
    ff = eval(f)
    # pos = 0
    pos = l_dict[w][0][1]
    print('pos', pos)
    pos_b = pos - 5
    pos_a = (pos + 1) + 5
    if pos_b >= 0 and pos_a <= len(ff):
        pre = ' '.join(ff[pos_b:pos])
        post = ' '.join(ff[pos+1:pos_a])
        out = (pre, post)
    return out
print(pp_sent('clear', 'l_00'))


def clinamen(word, i):
    out = set()
    items = [item for item in l_00
             if dameraulevenshtein(word, item) <= i]
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
            if (x > 0 and y > 0 and seq1[x] == seq2[y - 1] and
               seq1[x - 1] == seq2[y] and seq1[x] != seq2[y]):
                    thisrow[y] = min(thisrow[y], twoago[y - 2] + 1)
    return thisrow[len(seq2) - 1]


def sear(t):
    temp = l_dict.get(t)
    # print(temp)
    temp1 = []
    for f in temp:
        x = ''.join(['l_', str(f[0:2])])
        # print('fullsent:', f)
        # print(fullsent(t, x))
        temp1.append(x)
    return temp1

# print(sear('fingers'))
