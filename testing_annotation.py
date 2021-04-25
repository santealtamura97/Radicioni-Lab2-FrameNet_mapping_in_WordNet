#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:08:48 2021

@author: santealtamura
"""

from nltk.corpus import wordnet as wn
from nltk.corpus import framenet as fn

#TESTING FRAME NAME
f = fn.frame(1684)
print(f.definition)
regex = "Scrutinizing"
print("=================================================")
for synset in wn.synsets(regex):
    print("\n", synset, synset.definition())

