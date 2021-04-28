#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:08:48 2021

@author: santealtamura
"""

from nltk.corpus import wordnet as wn
from nltk.corpus import framenet as fn

"""
Attenzione: questo script è utile solo ai fini dello sviluppatore
come aiuto alla annotazione
"""

"""
#VALUTAZIONE FRAME NAME


f = fn.frame(153)
print("Process_stopped_state: ",f.definition)
regex = "stopped"


print("=================================================")
for synset in wn.synsets(regex):
    print("\n", synset, synset.definition()
    
#VALUTAZIONE FRAME ELEMENTS


print("=================================================")
frame_name = 'Duration'
fed = f.FE[frame_name]
print("Frame element definition: ",fed.definition)
print("=================================================")
for synset in wn.synsets(frame_name):
    print("\n", synset, synset.definition())


#VALUTAZIONE LEXICAL UNITS


print("=================================================")
lexical_unit_name = 'stash.n'
lud = f.lexUnit[lexical_unit_name]
print("Lexical unit definition: ",lud.definition)
print("=================================================")
for synset in wn.synsets('stash'):
    print("\n", synset, synset.definition())
"""