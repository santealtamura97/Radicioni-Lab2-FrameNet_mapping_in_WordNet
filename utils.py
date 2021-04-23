#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:24:19 2021

@author: santealtamura
"""
import string
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def context_for_frame(frame):
    context_frame = set()
    
    context_frame.update(pre_processing(frame.definition))
    
    FEs = frame.FE.keys()
    for fe in FEs:
        fed = frame.FE[fe]
        context_frame.update(pre_processing(fed.definition))
    
    LUs = frame.lexUnit.keys()
    for lu in LUs:
        lud = frame.lexUnit[lu]
        context_frame.update(pre_processing(lud.definition))
    
    return context_frame

def context_for_sense(sense):
    context_sense = set()
    
    context_sense.update(pre_processing(sense.definition()))
    for example in sense.examples():
        context_sense.update(pre_processing(example))
    
    for hypernym in sense.hypernyms():
        context_sense.update(pre_processing(hypernym.definition()))
        for example in hypernym.examples():
            context_sense.update(pre_processing(example))
            
    for hyponym in sense.hyponyms():
        context_sense.update(pre_processing(hyponym.definition()))
        for example in hyponym.examples():
            context_sense.update(pre_processing(example))
    return context_sense
        

#Rimuove le stopwords da una lista di parola
def remove_stopwords(words_list):
    stopwords_list = get_stopwords()
    new_words_list = []
    for word in words_list:
        word_lower = word.lower()
        if word_lower not in stopwords_list:
            new_words_list.append(word_lower)
    return new_words_list

#Rimuove la punteggiatura da una lista di parole
def remove_punctuation(words_list):
    new_words_list = []
    for word in words_list:
        temp = word
        if not temp.strip(string.punctuation) == "":
            new_word = word.lower()
            new_word = new_word.replace("'","")
            new_words_list.append(new_word)
    return new_words_list

#Restituisce la l'insieme di stopwords dal file delle stopwords
def get_stopwords():
    stopwords = open("stop_words_FULL.txt", "r")
    stopwords_list = []
    for word in stopwords:
        stopwords_list.append(word.replace('\n', ''))
    stopwords.close()
    return stopwords_list

def tokenize_sentence(sentence):
    words_list = []
    lmtzr = WordNetLemmatizer()
    for word in word_tokenize(sentence):
        words_list.append(lmtzr.lemmatize(word))
    return words_list

def pre_processing(sentence):
    return remove_stopwords(remove_punctuation(tokenize_sentence(sentence)))
