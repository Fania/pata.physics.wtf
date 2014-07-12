from flask import url_for
import os
import nltk
#import unicodedata as ud
import codecs
from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader
import sys
#print sys.getdefaultencoding()

# Ignore weird unicode warnings from dameraulevenshtein function
import warnings
warnings.simplefilter('ignore')

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
print book_list
troll = book_list.words('faustroll.txt')
faustroll = nltk.Text(troll)
############################################################

############################################################
# UNICODE TESTS
#bloy = book_list.words('04.bloy_french.txt')
#bloyfrench = nltk.Text(bloy)
#print bloyfrench[0:300]


# Fania's Non-NLTK way to import txt file
#path_b = os.path.join(root_path, 'corpus/04.bloy_french.txt')
#bloy_text = open(path_b, "r")
#bloytext = [i.lower() for line in bloy_text.readlines() for i in line.split()]
#print bloytext[0:100]
#bloy_text.close()
#
#bloycode = [i.encode('utf-8') for i in bloytext]
#bloy1 = bloycode
#print '++++++++++++++++++++'
#print bloy1[0:100]

# UNICODE TESTS

# Fania's Non-NLTK way to import txt file
#path_f = os.path.join(root_path, 'corpus/faustroll.txt')
#faustroll_text = open(path_f, "r")
#text = [i.lower() for line in faustroll_text.readlines() for i in line.split()]
#faustroll_text.close()
#faustroll = text

path_e = corpus_root + '/english'
print 'path_e ', path_e
stopwords_doc = open(path_e, "r")
sw = [i for line in stopwords_doc.readlines() for i in line.split()]
stopwords_doc.close()
#sw = stopwords.words('english')
# faustroll_dict = sorted(set([w.lower() for w in faustroll]))
faustroll_dict = sorted(set([w for w in faustroll]))
# froll_dict = [w.lower() for w in faustroll_dict if w.isalpha() and w.lower() not in sw]
froll_dict = [w for w in faustroll_dict if w.isalpha() not in sw]
# ud.normalize('NFKD', w).encode('ascii', 'ignore')


def syzygy(word):
    out = set()
    wordsets = wn.synsets(word)  # returns a list of synsets
    for w in wordsets:
        # Hyponyms share a type-of relationship with their hypernym
        print 'w', w
        hypo = w.hyponyms()  # returns a list of synsets
        for h in hypo:  # for every synset h
            print 'h', h
            for l in h.lemmas():
                print 'l', l
                if l.name in froll_dict:
                    out.add(l.name)
                    #print 'added hypo'
        # Hyponyms share a type-of relationship with their hypernym
        hyper = w.hypernyms()
        for h in hyper:
            for l in h.lemmas():
                if l.name in froll_dict:
                    out.add(l.name)
                    #print 'added hyper'
        # 'X' is a holonym of 'Y' if Ys are parts of Xs, or
        # 'X' is a holonym of 'Y' if Ys are members of Xs.
        holo = w.member_holonyms()
        for h in holo:
            for l in h.lemmas():
                if l.name in froll_dict:
                    out.add(l.name)
                    #print 'added holo'
    return out


def antinomy(word):
    out = set()
    wordsets = wn.synsets(word)
    for w in wordsets:
        anti = w.lemmas[0].antonyms()
        for a in anti:
            if a.name != word:
                out.add(a.name)
    return out


def find_sentence(word):
    #print faustroll.index('Anna')
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


# NLP Course - Coursera 2012
# Dan Jurafsky and Chris Manning
# Taken from http://mwh.geek.nz/2009/04/26/python-damerau-levenshtein-distance/
# MIT license.
def dameraulevenshtein(seq1, seq2):
    """Calculate the Damerau-Levenshtein distance between sequences.

    This distance is the number of additions, deletions, substitutions,
    and transpositions needed to transform the first sequence into the
    second. Although generally used with strings, any sequences of
    comparable objects will work.

    Transpositions are exchanges of *consecutive* characters; all other
    operations are self-explanatory.

    This implementation is O(N*M) time and O(M) space, for N and M the
    lengths of the two sequences.

    >>> dameraulevenshtein('ba', 'abc')
    2
    >>> dameraulevenshtein('fee', 'deed')
    2

    It works with arbitrary sequences too:
    >>> dameraulevenshtein('abcd', ['b', 'a', 'c', 'd', 'e'])
    2
    """
    # codesnippet:D0DE4716-B6E6-4161-9219-2903BF8F547F
    # Conceptually, this is based on a len(seq1) + 1 * len(seq2) + 1 matrix.
    # However, only the current and two previous rows are needed at once,
    # so we only store those.
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

#def get_concordances(word):
#    return faustroll.concordance(word)
#print get_concordances('skiff')
