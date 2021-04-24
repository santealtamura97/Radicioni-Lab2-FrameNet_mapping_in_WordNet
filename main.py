#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:24:11 2021

@author: santealtamura
"""

from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn
import utils

SURNAME = 'Altamura'

def get_contexts_frames_list(frames):
    contexts_frames_list = []
    for frame in frames:
      
        #dati riguardanti i frame elements e le lexical units del frame
        frame_elements_contexts = dict()
        lexical_units_contexts = dict()
        
        FEs = frame.FE.keys()
        for fe in FEs:
            fed = frame.FE[fe]
            frame_elements_contexts[fed.name] = utils.context_for_frame_component(fed)
            
        LUs = frame.lexUnit.keys()
        for lu in LUs:
            lud = frame.lexUnit[lu]
            lexical_units_contexts[lud.name] = utils.context_for_frame_component(lud)
        
        contextsFrame = utils.ContextsFrame(frame.ID, frame.name, utils.context_for_frame(frame), 
                                            frame_elements_contexts, lexical_units_contexts)
        contexts_frames_list.append(contextsFrame) 
    return contexts_frames_list

#restituisce un senso di WordNet per il frameNet_name(frame name, frame element name, lexical unit name)
#che massimizza lo score
def compute_score(frameNet_name, frameNet_context):
    wordnet_name = utils.get_regent(frameNet_name)
    synsets = wn.synsets(wordnet_name)
    if synsets == []:
        return None
    #prende il synset con lo score più alto
    max_score = 0
    best_synset = synsets[0]
    for synset in synsets:
        synset_context = utils.context_for_sense(synset)
        score = get_score(frameNet_context,synset_context)
        if score > max_score:
            max_score = score
            best_synset = synset
    return best_synset

def get_score(context1,context2):
    return len(context1.intersection(context2)) + 1
    

def get_synsets_frames_list(contexts_frame_list):
    for contextsFrame in contexts_frame_list:
        frame_synset = compute_score(contextsFrame.get_frame_name(),
                                     contextsFrame.get_frame_context())
        frame_elements_synsets = dict()
        #lexical_units_synsets = dict()
        frame_elements_contexts = contextsFrame.get_frame_elements_contexts()
        for frame_element_name in frame_elements_contexts:
            score = compute_score(frame_element_name, frame_elements_contexts[frame_element_name])
            if not type(score) == None:
               frame_elements_synsets[frame_element_name] = score
               
        #test
        print("=====================")
        print(frame_synset)
        print(frame_elements_synsets)
        
def main():
    #Lista di oggetti ti tipo ContextsFrame
    contexts_frames_list = get_contexts_frames_list(utils.getFrameSetForStudent(SURNAME))
    get_synsets_frames_list(contexts_frames_list)
    
main()
