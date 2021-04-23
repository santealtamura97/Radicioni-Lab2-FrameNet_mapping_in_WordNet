#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:24:11 2021

@author: santealtamura
"""

from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn
import utils


"""
frame_name = "scrutizing_for"
frame_name = frame_name.replace("_"," ")
tokens = nltk.word_tokenize(frame_name)
print("Tokens: ",tokens)
print("Pos tag: ",nltk.pos_tag(tokens))
"""

#print(fn.frames('Process_stopped_state')[0])
print(utils.context_for_frame(fn.frame_by_name('Cache')))
print()
print(utils.context_for_sense(wn.synsets('Cache')[0]))