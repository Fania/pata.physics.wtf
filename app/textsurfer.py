from __future__ import print_function

from nltk.corpus import wordnet as wn
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

from collections import defaultdict

import os
import re
import time, datetime
#############################################

root_path = os.path.dirname(os.path.abspath(__file__))
root_path = root_path[:-4]
corpus_root = root_path + '/app/static/corpus'
faust_root = corpus_root + '/faustroll'
shake_root = corpus_root + '/shakespeare'
library = PlaintextCorpusReader(faust_root, '.*\.txt')  # root, fileid
slibrary = PlaintextCorpusReader(shake_root, '.*\.txt')  # root, fileid

############################################################
l_00 = library.words('00.faustroll.txt')
l_01 = library.words('01.poe1.txt')
l_02 = library.words('02.bergerac.txt')
l_03 = library.words('03.gospel.txt')
l_04 = library.words('04.bloy_french.txt')
l_05 = library.words('05.coleridge.txt')
l_06 = library.words('06.darien_french.txt')
l_07 = library.words('07.desbordes_french.txt')
l_08 = library.words('08.elskamp_french.txt')
l_09 = library.words('09.florian_french.txt')
l_10 = library.words('10.arabiannights.txt')
l_11 = library.words('11.grabbe_german.txt')
l_12 = library.words('12.kahn_french.txt')
l_13 = library.words('13.lautreamont_french.txt')
l_14 = library.words('14.maeterlinck.txt')
l_15 = library.words('15.mallarme_french.txt')
l_16 = library.words('16.mendes.txt')
l_17 = library.words('17.odyssey.txt')
l_18 = ''
l_19 = library.words('19.rabelais.txt')
l_20 = ''
l_21 = ''
l_22 = library.words('22.rimbaud_french.txt')
l_23 = library.words('23.schwob_german.txt')
l_24 = library.words('24.ubu_french.txt')
l_25 = library.words('25.verlaine.txt')
l_26 = library.words('26.verhaeren.txt')
l_27 = library.words('27.verne.txt')
############################################
en_stop = stopwords.words('english')
fr_stop = stopwords.words('french')
de_stop = stopwords.words('german')
############################################################
s_00 = slibrary.words('00.sonnets.txt')
s_01 = slibrary.words('01.alls_well.txt')
s_02 = slibrary.words('02.antony_cleopatra.txt')
s_03 = slibrary.words('03.as_you_like_it.txt')
s_04 = slibrary.words('04.comedy_of_errors.txt')
s_05 = slibrary.words('05.coriolanus.txt')
s_06 = slibrary.words('06.cymbeline.txt')
s_07 = slibrary.words('07.hamlet.txt')
s_08 = slibrary.words('08.king_henry_IV_1.txt')
s_09 = slibrary.words('09.king_henry_IV_2.txt')
s_10 = slibrary.words('10.king_henry_V.txt')
s_11 = slibrary.words('11.king_henry_VI_1.txt')
s_12 = slibrary.words('12.king_henry_VI_2.txt')
s_13 = slibrary.words('13.king_henry_VI_3.txt')
s_14 = slibrary.words('14.king_henry_VIII.txt')
s_15 = slibrary.words('15.king_john.txt')
s_16 = slibrary.words('16.julius_caesar.txt')
s_17 = slibrary.words('17.king_lear.txt')
s_18 = slibrary.words('18.loves_labours_lost.txt')
s_19 = slibrary.words('19.macbeth.txt')
s_20 = slibrary.words('20.measure_for_measure.txt')
s_21 = slibrary.words('21.merchant_of_venice.txt')
s_22 = slibrary.words('22.merry_wives_of_windsor.txt')
s_23 = slibrary.words('23.midsummer_nights_dream.txt')
s_24 = slibrary.words('24.much_ado_about_nothing.txt')
s_25 = slibrary.words('25.othello.txt')
s_26 = slibrary.words('26.king_richard_II.txt')
s_27 = slibrary.words('27.king_richard_III.txt')
s_28 = slibrary.words('28.romeo_and_juliet.txt')
s_29 = slibrary.words('29.taming_of_the_shrew.txt')
s_30 = slibrary.words('30.tempest.txt')
s_31 = slibrary.words('31.timon_of_athens.txt')
s_32 = slibrary.words('32.titus_andronicus.txt')
s_33 = slibrary.words('33.troilus_and_cressida.txt')
s_34 = slibrary.words('34.twelfth_night.txt')
s_35 = slibrary.words('35.two_gentlemen_of_verona.txt')
s_36 = slibrary.words('36.winters_tale.txt')
s_37 = slibrary.words('37.lovers_complaint.txt')



l_dict = defaultdict(lambda: defaultdict(list))
s_dict = defaultdict(lambda: defaultdict(list))


# l_dict structure:
# {word1: {fileA: [pos1, pos2, ...], fileB: [pos], ...},
#  word2: {fileC: [pos1, pos2], fileK: [pos], ...},
#  ...
# }


def setupcorpus(f, lang, dic, d):
    # x = counter, w = word in file f, dic = index dictionary
    for x, w in enumerate(f):
        if w.isalpha() and (w.lower() not in lang):
            y = d + '_' + (re.search(r"((\d\d).(\w)+.txt)", f.fileid)).group(2)
            dic[w.lower()][y].append(x)


setupcorpus(l_00, en_stop, l_dict, 'l'), print('added 00 - FT')
setupcorpus(l_01, en_stop, l_dict, 'l'), print('added 01 - FT')
setupcorpus(l_02, en_stop, l_dict, 'l'), print('added 02 - FT')
setupcorpus(l_03, en_stop, l_dict, 'l'), print('added 03 - FT')
setupcorpus(l_04, fr_stop, l_dict, 'l'), print('added 04 - FT')
setupcorpus(l_05, en_stop, l_dict, 'l'), print('added 05 - FT')
setupcorpus(l_06, fr_stop, l_dict, 'l'), print('added 06 - FT')
setupcorpus(l_07, en_stop, l_dict, 'l'), print('added 07 - FT')
setupcorpus(l_08, fr_stop, l_dict, 'l'), print('added 08 - FT')
setupcorpus(l_09, fr_stop, l_dict, 'l'), print('added 09 - FT')
setupcorpus(l_10, en_stop, l_dict, 'l'), print('added 10 - FT')
setupcorpus(l_11, en_stop, l_dict, 'l'), print('added 11 - FT')
setupcorpus(l_12, fr_stop, l_dict, 'l'), print('added 12 - FT')
setupcorpus(l_13, fr_stop, l_dict, 'l'), print('added 13 - FT')
setupcorpus(l_14, en_stop, l_dict, 'l'), print('added 14 - FT')
setupcorpus(l_15, fr_stop, l_dict, 'l'), print('added 15 - FT')
setupcorpus(l_16, en_stop, l_dict, 'l'), print('added 16 - FT')
setupcorpus(l_17, en_stop, l_dict, 'l'), print('added 17 - FT')
setupcorpus(l_18, en_stop, l_dict, 'l'), print('added 18 - FT')
setupcorpus(l_19, en_stop, l_dict, 'l'), print('added 19 - FT')
setupcorpus(l_20, en_stop, l_dict, 'l'), print('added 20 - FT')
setupcorpus(l_21, en_stop, l_dict, 'l'), print('added 21 - FT')
setupcorpus(l_22, fr_stop, l_dict, 'l'), print('added 22 - FT')
setupcorpus(l_23, de_stop, l_dict, 'l'), print('added 23 - FT')
setupcorpus(l_24, fr_stop, l_dict, 'l'), print('added 24 - FT')
setupcorpus(l_25, en_stop, l_dict, 'l'), print('added 25 - FT')
setupcorpus(l_26, en_stop, l_dict, 'l'), print('added 26 - FT')
setupcorpus(l_27, en_stop, l_dict, 'l'), print('added 27 - FT')

setupcorpus(s_00, en_stop, s_dict, 's'), print('added 00 - SH')
setupcorpus(s_01, en_stop, s_dict, 's'), print('added 01 - SH')
setupcorpus(s_02, en_stop, s_dict, 's'), print('added 02 - SH')
setupcorpus(s_03, en_stop, s_dict, 's'), print('added 03 - SH')
setupcorpus(s_04, en_stop, s_dict, 's'), print('added 04 - SH')
setupcorpus(s_05, en_stop, s_dict, 's'), print('added 05 - SH')
setupcorpus(s_06, en_stop, s_dict, 's'), print('added 06 - SH')
setupcorpus(s_07, en_stop, s_dict, 's'), print('added 07 - SH')
setupcorpus(s_08, en_stop, s_dict, 's'), print('added 08 - SH')
setupcorpus(s_09, en_stop, s_dict, 's'), print('added 09 - SH')
setupcorpus(s_10, en_stop, s_dict, 's'), print('added 10 - SH')
setupcorpus(s_11, en_stop, s_dict, 's'), print('added 11 - SH')
setupcorpus(s_12, en_stop, s_dict, 's'), print('added 12 - SH')
setupcorpus(s_13, en_stop, s_dict, 's'), print('added 13 - SH')
setupcorpus(s_14, en_stop, s_dict, 's'), print('added 14 - SH')
setupcorpus(s_15, en_stop, s_dict, 's'), print('added 15 - SH')
setupcorpus(s_16, en_stop, s_dict, 's'), print('added 16 - SH')
setupcorpus(s_17, en_stop, s_dict, 's'), print('added 17 - SH')
setupcorpus(s_18, en_stop, s_dict, 's'), print('added 18 - SH')
setupcorpus(s_19, en_stop, s_dict, 's'), print('added 19 - SH')
setupcorpus(s_20, en_stop, s_dict, 's'), print('added 20 - SH')
setupcorpus(s_21, en_stop, s_dict, 's'), print('added 21 - SH')
setupcorpus(s_22, en_stop, s_dict, 's'), print('added 22 - SH')
setupcorpus(s_23, en_stop, s_dict, 's'), print('added 23 - SH')
setupcorpus(s_24, en_stop, s_dict, 's'), print('added 24 - SH')
setupcorpus(s_25, en_stop, s_dict, 's'), print('added 25 - SH')
setupcorpus(s_26, en_stop, s_dict, 's'), print('added 26 - SH')
setupcorpus(s_27, en_stop, s_dict, 's'), print('added 27 - SH')
setupcorpus(s_28, en_stop, s_dict, 's'), print('added 28 - SH')
setupcorpus(s_29, en_stop, s_dict, 's'), print('added 29 - SH')
setupcorpus(s_30, en_stop, s_dict, 's'), print('added 30 - SH')
setupcorpus(s_31, en_stop, s_dict, 's'), print('added 31 - SH')
setupcorpus(s_32, en_stop, s_dict, 's'), print('added 32 - SH')
setupcorpus(s_33, en_stop, s_dict, 's'), print('added 33 - SH')
setupcorpus(s_34, en_stop, s_dict, 's'), print('added 34 - SH')
setupcorpus(s_35, en_stop, s_dict, 's'), print('added 35 - SH')
setupcorpus(s_36, en_stop, s_dict, 's'), print('added 36 - SH')
setupcorpus(s_37, en_stop, s_dict, 's'), print('added 37 - SH')

# print(s_dict)

# print(len(l_dict), len(s_dict))
# with open("dict.txt", "a") as mylog:
#     mylog.write(str(l_dict))
#     mylog.write('\n')
#     mylog.write(str(s_dict))

def get_results(words, algo, dic):
    total = 0
    out, sources = set(), set()
    for r in words:
        if dic == 'faustroll': files = l_dict[r]
        else: files = s_dict[r]
        for e, p in files.items():
            f = get_title(e)
            sources.add(f)
            # first occurance
            o = (f, pp_sent(r.lower(), e, p), algo)
            total += 1
            out.add(o)
            # each occurance
            # sents = pp_sent(r.lower(), e, p)
            # for s in sents:
            #     o = (f, s, algo)
            #     if s != [] and o not in out:
            #         total += 1
            #         out.add(o)
    return out, sources, total


def get_nym(nym, wset):
    out = []
    hhh = wset.hyponyms()
    if nym == 'hypo':
        hhh = wset.hyponyms()
    if nym == 'hyper':
        hhh = wset.hypernyms()
    if nym == 'holo':
        hhhm = wset.member_holonyms()
        hhhs = wset.substance_holonyms()
        hhhp = wset.part_holonyms()
        hhh = hhhm + hhhs + hhhp
    if nym == 'mero':
        hhhm = wset.member_meronyms()
        hhhs = wset.substance_meronyms()
        hhhp = wset.part_meronyms()
        hhh = hhhm + hhhs + hhhp
    if len(hhh) > 0:
        for h in hhh:
            for l in h.lemmas():
                out.append(str(l.name()))
                # ts = time.time()
                # st = datetime.datetime.fromtimestamp(ts).strftime('%d%m%y%H%M%S')
                # p = nym + ", " + str(wset) + ", " + l.name() + "\n"
                # f = "thesis" + st + ".txt"
                # with open(f, "a") as mylog:
                #     mylog.write(p)
    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%d%m%y%H%M%S')
    # p = nym + ", " + str(wset) + ", " + str(len(hhh)) + "\n"
    # f = "syzygy" + st + ".txt"
    # with open(f, "a") as mylog:
    #     mylog.write(p)
    return out


def clinamen(w, c, i):
    # l_00 is the faustroll text
    # l_10 is arabian nights
    # s_23 is midsummer nights dream
    # words = set([item for item in l_00
    # wordsMND = set([item for item in s_23
    #             if dameraulevenshtein(w, item) <= i])
    # wordsAN = set([item for item in l_10
    #             if dameraulevenshtein(w, item) <= i])
    words = set([item for item in l_00
                if dameraulevenshtein(w, item) <= i])
    out, sources, total = get_results(words, 'Clinamen', c)
    
    # t = 'clinamen: MND = %s' % wordsMND
    # s = 'clinamen: AN = %s' %wordsAN
    # f = 'clinamen: F = %s' % words
    # with open("thesis.txt", "a") as mylog:
        # mylog.write(t)
        # mylog.write('\n')
        # mylog.write(s)
        # mylog.write('\n')
        # mylog.write(f)
        # mylog.write('\n')
    return out, words, sources, total


def syzygy(w, c):
    words = set()
    hypos = set()
    hypers = set()
    holos = set()
    meros = set()
    wordsets = wn.synsets(w)
    hypo_len, hyper_len, holo_len, mero_len, syno_len = 0,0,0,0,0
    for ws in wordsets:
        hypos.update(get_nym('hypo', ws))
        hypo_len += len(hypos)
        words.update(hypos)
        hypers.update(get_nym('hyper', ws))
        hyper_len += len(hypers)
        words.update(hypers)
        holos.update(get_nym('holo', ws))
        holo_len += len(holos)
        words.update(holos)
        meros.update(get_nym('mero', ws))
        mero_len += len(meros)
        words.update(meros)
        syno_len += 1
    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%d%m%y%H%M%S')
    # p0 = w + " - synos: " + str(wordsets) + "\n"
    # p1 = w + " - hypos: " + str(hypos) + "\n"
    # p2 = w + " - hypers: " + str(hypers) + "\n"
    # p3 = w + " - holos: " + str(holos) + "\n"
    # p4 = w + " - meros: " + str(meros) + "\n"
    # f = "syzygy" + st + ".txt"
    # with open(f, "a") as mylog:
    #     mylog.write(p0)
    #     mylog.write(p1)
    #     mylog.write(p2)
    #     mylog.write(p3)
    #     mylog.write(p4)
    # print('inside syzygy function: ', words)
    out, sources, total = get_results(words, 'Syzygy', c)
    return out, words, sources, total


def antinomy(w, c):
    words = set()
    wordsets = wn.synsets(w)
    for ws in wordsets:
        anti = ws.lemmas()[0].antonyms()
        if len(anti) > 0:
            for a in anti:
                if str(a.name()) != w:
                    words.add(str(a.name()))
    out, sources, total = get_results(words, 'Antinomy', c)
    return out, words, sources, total


def get_title(file):
    return {
        'l_00': 'Alfred Jarry: Exploits and Opinions of Dr. Faustroll, Pataphysician',
        'l_01': 'Edgar Allen Poe: Collected Works',
        'l_02': 'Cyrano de Bergerac: A Voyage to the Moon',
        'l_03': 'Saint Luke: The Gospel',
        'l_04': 'Leon Bloy: Le Desespere',
        'l_05': 'Samuel Taylor Coleridge: The Rime of the Ancient Mariner',
        'l_06': 'Georges Darien: Le Voleur',
        'l_07': 'Marceline Desbordes-Valmore: Le Livre des Meres et des Enfants',
        'l_08': 'Max Elskamp: Enluminures',
        'l_09': 'Jean-Pierre Claris de Florian: Les Deux Billets',
        'l_10': 'One Thousand and One Nights',
        'l_11': 'Christian Dietrich Grabbe: Scherz, Satire, Ironie und tiefere Bedeutung',
        'l_12': "Gustave Kahn: Le Conte de l'Or et Du Silence",
        'l_13': 'Le Comte de Lautreamont: Les Chants de Maldoror',
        'l_14': 'Maurice Maeterlinck: Aglavaine and Selysette',
        'l_15': 'Stephane Mallarme: Verse and Prose',
        'l_16': 'Mendes: The Mirror and la Divina Aventure',
        'l_17': 'Homer: The Odyssey',
        'l_18': 'Josephin Peladan: Babylon',
        'l_19': 'Francois Rabelais: Gargantua and Pantagruel',
        'l_20': "Jean de Chilra: L'Heure Sexuelle",
        'l_21': 'Henri de Regnier: La Canne de Jaspe',
        'l_22': 'Arthur Rimbaud: Poesies Completes',
        'l_23': 'Marcel Schwob: Der Kinderkreuzzug',
        'l_24': 'Alfred Jarry: Ubu Roi',
        'l_25': 'Paul Verlaine: Poems',
        'l_26': 'Emile Verhaeren: Poems',
        'l_27': 'Jules Verne: A Journey to the Centre of the Earth',
        's_00': 'William Shakespeare, 1609: The Sonnets',
        's_01': 'William Shakespeare, 1603: Alls Well That Ends Well',
        's_02': 'William Shakespeare, 1607: The Tragedy of Antony and Cleopatra',
        's_03': 'William Shakespeare, 1601: As You Like It',
        's_04': 'William Shakespeare, 1593: The Comedy of Errors',
        's_05': 'William Shakespeare, 1608: The Tragedy of Coriolanus',
        's_06': 'William Shakespeare, 1609: Cymbeline',
        's_07': 'William Shakespeare, 1604: The Tragedy of Hamlet, Prince of Denmark',
        's_08': 'William Shakespeare, 1598: The First Part of King Henry the Fourth',
        's_09': 'William Shakespeare, 1598: The Second Part of King Henry the Fourth',
        's_10': 'William Shakespeare, 1599: The Life of Kind Henry the Fifth',
        's_11': 'William Shakespeare, 1592: The First Part of Henry the Sixth',
        's_12': 'William Shakespeare, 1592: The Second Part of Henry the Sixth',
        's_13': 'William Shakespeare, 1592: The Third Part of Henry the Sixth',
        's_14': 'William Shakespeare, 1611: King Henry the Eigth',
        's_15': 'William Shakespeare, 1597: King John',
        's_16': 'William Shakespeare, 1599: The Tragedy of Julius Caesar',
        's_17': 'William Shakespeare, 1606: The Tragedy of King Lear',
        's_18': "William Shakespeare, 1595: Love's Labour's Lost",
        's_19': 'William Shakespeare, 1606: The Tragedy of Macbeth',
        's_20': 'William Shakespeare, 1605: Measure for Measure',
        's_21': 'William Shakespeare, 1597: The Merchant of Venice',
        's_22': 'William Shakespeare, 1601: The Merry Wives of Windsor',
        's_23': "William Shakespeare, 1596: A Midsummer Night's Dream",
        's_24': 'William Shakespeare, 1599: Much Ado About Nothing',
        's_25': 'William Shakespeare, 1605: The Tragedy of Othello, Moor of Venice',
        's_26': 'William Shakespeare, 1596: King Richard the Second',
        's_27': 'William Shakespeare, 1593: Kind Richard III',
        's_28': 'William Shakespeare, 1595: The Tragedy of Romeo and Juliet',
        's_29': 'William Shakespeare, 1594: The Taming of the Shrew',
        's_30': 'William Shakespeare, 1612: The Tempest',
        's_31': 'William Shakespeare, 1608: The Life of Timon of Athens',
        's_32': 'William Shakespeare, 1594: The Tragedy of Titus Andronicus',
        's_33': 'William Shakespeare, 1602: The History of Troilus and Cressida',
        's_34': 'William Shakespeare, 1602: Twelfth Night or What You Will',
        's_35': 'William Shakespeare, 1595: The Two Gentlemen of Verona',
        's_36': "William Shakespeare, 1611: The Winter's Tale",
        's_37': "William Shakespeare, 1609: A Lover's Complaint"
    }.get(file, 'Unknown')  # 'Unknown' is default if file not found


def pp_sent(w, f, p):  # gets w as lower case
    # w = word, f = file, p = [positions]
    # print('pp_sent', w, f, p)

    # FIRST OCCURENCE
    out, pos = [], p[0] # FIRST OCCURENCE
    ff = eval(f)
    pos_b, pos_a = pos, pos
    punct = [',', '.', '!', '?', '(', ')', ':', ';', '\n', '-', '_']
    for i in range(1, 10):
        if pos > i:
            if ff[pos - i] in punct:
                pos_b = pos - (i - 1)
                break
            else:
                if ff[pos - 5]:
                    pos_b = pos - 5
                else:
                    pos_b = pos
        else:
            pos_b = pos
    for j in range(1, 10):
        if (pos + j) < len(ff):
            if ff[pos + j] in punct:
                pos_a = pos + j
                break
            else:
                if ff[pos + j]:
                    pos_a = pos + j
                else:
                    pos_a = pos
        else:
          pos_a = pos
    if pos_b >= 0 and pos_a <= len(ff):
        pre = ' '.join(ff[pos_b:pos])
        post = ' '.join(ff[pos+1:pos_a])
        out = (pre, w, post)
        # print("pp_sent", out)

    # EACH OCCURANCE
    # oout = []
    # for x in p:
    #     out, pos = [], x # EACH OCCURANCE
    #     ff = eval(f)
    #     pos_b, pos_a = pos, pos
    #     punct = [',', '.', '!', '?', '(', ')', ':', ';', '\n', '-', '_']
    #     for i in range(1, 10):
    #         if pos > i:
    #             if ff[pos - i] in punct:
    #                 pos_b = pos - (i - 1)
    #                 break
    #             else:
    #                 if ff[pos - 5]:
    #                     pos_b = pos - 5
    #                 else:
    #                     pos_b = pos
    #         else:
    #             pos_b = pos
    #     for j in range(1, 10):
    #         if (pos + j) < len(ff):
    #             if ff[pos + j] in punct:
    #                 pos_a = pos + j
    #                 break
    #             else:
    #                 # print(len(ff), pos+5)
    #                 if ff[pos + j]:
    #                     pos_a = pos + j
    #                 else:
    #                     pos_a = pos
    #         else:
    #             pos_a = pos
    #     if pos_b >= 0 and pos_a <= len(ff):
    #         pre = ' '.join(ff[pos_b:pos])
    #         post = ' '.join(ff[pos+1:pos_a])
    #         out = (pre, w, post)
    #         # print("pp_sent", out)
    #         oout.append(out)

    # one = "pp_sent "
    # two = (w,f,p)
    # three = "sentence "
    # four = one + str(two) + three + str(out) + "\n"
    # with open("ppsent3.txt", "a") as mylog:
    #     mylog.write(four)
    return out


# http://mwh.geek.nz/2009/04/26/python-damerau-levenshtein-distance/
# MIT license.
def dameraulevenshtein(seq1, seq2):
    oneago = None
    thisrow = range(1, len(seq2) + 1) + [0]
    for x in xrange(len(seq1)):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in xrange(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
            if (x > 0 and y > 0 and seq1[x] == seq2[y - 1] and
               seq1[x - 1] == seq2[y] and seq1[x] != seq2[y]):
                    thisrow[y] = min(thisrow[y], twoago[y - 2] + 1)
    return thisrow[len(seq2) - 1]


# sens = all_sens
def calc_all(sens):
    # not needed all these all_x variables
    all_1, all_2, all_3, all_4, all_5, all_6, all_7, all_8, all_9, \
        all_10, all_11, all_12, all_13, all_14 = [[] for _ in range(14)]
    out, b, part, mx = [], 0, 0, 15
    if len(sens) / 14 >= 1:
        part = len(sens) / 14
    else:
        part = 1
        mx = len(sens) + 1
    for i in range(1, mx):
        n = b + part
        v = eval('all_' + str(i)) # not needed
        v = sens[b:n]
        b += part
        out.append(v)
    return out, part, (mx - 1)

# out (lol) = all_sens divided into 14 lists
# all_poems = part ** mx  # no of options ^ no of lines
# all_sens = [(f, pp_sent(r.lower(), e, p), algo),...]
