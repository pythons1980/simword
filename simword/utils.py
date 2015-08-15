# -*- coding: utf-8 -*-
import functools
from fuzzywuzzy import fuzz


def most_similar_word(word, words):
    tuples = zip(map(functools.partial(fuzz.ratio, s2=word), words), words)
    return sorted(tuples, key=lambda a: a[0], reverse=True)[0]
