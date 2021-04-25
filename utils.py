#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:24:19 2021

@author: santealtamura
"""
import string
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import hashlib
import random
from random import randint
from random import seed
from nltk.corpus import framenet as fn
import spacy
from nltk.corpus import wordnet as wn
import nltk
#spacy.cli.download("en_core_web_sm")

#Contesti associati ad un Frame. Struttura dati che contiene
#i contesti associati al frame, ai suoi frame elements e alle sue
#lexical units
class ContextsFrame:
    
    def __init__(self, frame_id, frame_name, frame_context,
                 frame_elements_contexts, lexical_units_contexts):
        self.frame_id = frame_id
        self.frame_name = frame_name
        self.frame_context = frame_context
        #dizionario: [frame_element_name] -> context
        self.frame_elements_contexts = frame_elements_contexts
        
        #dizionario: [lexical_unit_name] -> context
        self.lexical_units_contexts = lexical_units_contexts
        
    def get_frame_elements_contexts(self):
        return self.frame_elements_contexts
    def get_lexical_units_contexts(self):
        return self.lexical_units_contexts
    def get_frame_id(self):
        return self.frame_id
    def get_frame_name(self):
        return self.frame_name
    def get_frame_context(self):
        return self.frame_context
    #stampa fatta al solo scopo di conoscere le struttura interna della classe
    def printContextsFrame(self):
        print("FRAME ID: ", self.get_frame_id())
        print("FRAME NAME: ",self.get_frame_name())
        print("\nFRAME CONTEXT: ","\n",self.get_frame_context())
        print("\nFRAME ELEMENTS CONTEXTS: ","\n", self.get_frame_elements_contexts())
        print("\nLEXICAL UNTIS CONTEXTS: ","\n", self.get_lexical_units_contexts())
        
    
#Risultati di WordNet.
#Struttura che contiene i synset associati al frame in questione
#ai suoi frame elements e alle sue lexical_units
#Questi risultati dovranno poi essere confrontati con 
#annotazioni fatte degli umani
#quindi ogni annotazione per ogni frame dovrà essere di questo tipo
#e.s SynsetsFrameAnnotation
class SynsetsFrame:
    def __init__(self, frame_id, frame_name, frame_synset,
                 frame_elements_synsets, lexical_units_synsets):
        self.frame_id = frame_id
        self.frame_name = frame_name
        self.frame_synset = frame_synset
        self.frame_elements_synsets = frame_elements_synsets
        self.lexical_units_synsets = lexical_units_synsets
    def get_frame_elements_synsets(self):
        return self.frame_elements_synsets
    def get_lexical_units_synsets(self):
        return self.lexical_units_synsets
    def get_frame_id(self):
        return self.frame_id
    def get_frame_name(self):
        return self.frame_name
    def get_frame_synset(self):
        return self.frame_synset
    #stampa fatta al solo scopo di conoscere le struttura interna della classe
    def printSynsetsFrame(self):
        print("FRAME ID: ", self.get_frame_id())
        print("FRAME NAME: ",self.get_frame_name())
        print("\nFRAME SYNSET: ",self.get_frame_synset())
        print("\nFRAME ELEMENTS SYNSETS: ","\n", self.get_frame_elements_synsets())
        print("\nLEXICAL UNTIS SYNSETS: ","\n", self.get_lexical_units_synsets())

def print_frames_with_IDs():
    for x in fn.frames():
        print('{}\t{}'.format(x.ID, x.name))

def get_frams_IDs():
    return [f.ID for f in fn.frames()]   

#restituisce un insieme di 5 frame legati allo studente in input ('Altamura')
def getFrameSetForStudent(surname, list_len=5):
    nof_frames = len(fn.frames())
    base_idx = (abs(int(hashlib.sha512(surname.encode('utf-8')).hexdigest(), 16)) % nof_frames)
    print('\nstudent: ' + surname + "\n")
    framenet_IDs = get_frams_IDs()
    i = 0
    offset = 0 
    seed(1)
    frame_list = []
    while i < list_len:
        fID = framenet_IDs[(base_idx+offset)%nof_frames]
        f = fn.frame(fID)
        frame_list.append(fn.frame(fID))
        fNAME = f.name
        #print('\tID: {a:4d}\tframe: {framename}'.format(a=fID, framename=fNAME))
        offset = randint(0, nof_frames)
        i += 1
    return frame_list        

#Prende in input un frame di FrameNet e restituisce il suo contesto
#formato da tutte le definizioni dei suoi frame element, lexical unit
#e del frame stesso. Le frasi sono tutte pre-processate
#in modo tale da ottenere un set di parole lemmatizzate, senza stopwords
#senza punteggiatura
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

#Restituisce il contesto per un frame component (frame element o lexical unit)
#che è praticamente formato dalla sua definizione, lemmatizzata,
#da cui sono state rimosse le stop words e punteggiatura
def context_for_frame_component(frame_component):
    context_frame_component = set()
    
    context_frame_component.update(pre_processing(frame_component.definition))
    
    return context_frame_component

#Prende in input un senso di WordNet e restituisce il suo contesto
#formato da tutte le definizioni ed esempi dei suoi iperonimi, iponimi
# e definizione ed esempi del senso stesso. Le frasi sono tutte pre-processate
#in modo tale da ottenere un set di parole lemmatizzate, senza stopwords
#senza punteggiatura
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

#riceve in input una frase semplice(costituita da circa due parole separate da _)
#e restituisce in output il reggente della frase
def get_regent(sentence):
    nlp = spacy.load("en_core_web_sm")
    #nlp = en_core_web_sm.load()
    if("_" in sentence or "-" in sentence):            
        sentence = sentence.replace("_", " ")
        sentence = sentence.replace("-", " ")
         #se la multiword ha un senso in WordNet, non è necessario individuare il reggente dell'espressione
        if(wn.synsets(sentence) == []):
            doc = nlp(sentence)
            chunks = list(doc.noun_chunks)
            try:
                chunk = chunks[0]
                regent = chunk.root.text
            except IndexError:
                regent = sentence.split(" ")[0]
        else:
             regent = sentence
    else:
        regent = sentence
    return regent

#Le unità lessicali ricavate da FrameNet per un determinato frame sono nella forma <ul>.PoS (esempio: before.prep)
#pertanto, per poter individuare il senso o i sensi corrispondenti all'unità lessicale, è importante rimuovere
#il punto e il PoS che segue
def remove_pos_lu(lexical_unit_name):
    new_lexical_unit_name = lexical_unit_name.split(".")[0]
    
    #Remove [...] from lexical_unit_name
    return new_lexical_unit_name.split(" [")[0]
    
    

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
    for tag in nltk.pos_tag(word_tokenize(sentence)):
        if (tag[1][:2] == "NN"):
            words_list.append(lmtzr.lemmatize(tag[0], pos = wn.NOUN))
        elif (tag[1][:2] == "VB"):
             words_list.append(lmtzr.lemmatize(tag[0], pos = wn.VERB))
        elif (tag[1][:2] == "RB"):
             words_list.append(lmtzr.lemmatize(tag[0], pos = wn.ADV))
        elif (tag[1][:2] == "JJ"):
             words_list.append(lmtzr.lemmatize(tag[0], pos = wn.ADJ))
    return words_list
    

def pre_processing(sentence):
    return remove_stopwords(remove_punctuation(tokenize_sentence(sentence)))
