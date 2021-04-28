#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:54:17 2021

@author: santealtamura
"""

from nltk.corpus import wordnet as wn
import utils

"""

student: Altamura
	ID:  153	      frame: Process_stopped_state
	ID:   10          frame: Transitive_action
	ID: 2411    	  frame: Personal_success
	ID: 1684    	  frame: Scrutinizing_for
	ID: 2576	      frame: Cache
"""

def get_synsets_frames_list_annotations():
    
    synsets_frames_list_annotations = []
    
    #-------------------------------------------------------------#
    frame_id_1 = 153
    frame_name_1 = 'Process_stopped_state'
    
    #Frame_name
    frame_synset_1 = wn.synset('discontinue.v.01')
    
    #FEs
    frame_elements_synsets_1 = dict()
    frame_elements_synsets_1['Process'] = wn.synset('process.n.06')
    frame_elements_synsets_1['Time'] = wn.synset('time.n.01')
    frame_elements_synsets_1['Duration'] = wn.synset('duration.n.03')
    
    #LUs
    lexical_units_synsets_1 = dict()
    
    synsets_frame_1 = utils.SynsetsFrame(frame_id_1, frame_name_1, frame_synset_1, 
                                       frame_elements_synsets_1, lexical_units_synsets_1)
    
    synsets_frames_list_annotations.append(synsets_frame_1)
    
    #-------------------------------------------------------------#
    frame_id_2 = 10
    frame_name_2 = "Transitive_action"
    
    #Frame_name
    frame_synset_2 = wn.synset('action.n.01')
    
    #FEs
    frame_elements_synsets_2 = dict()
    frame_elements_synsets_2['Agent'] = wn.synset('agent.n.02')
    frame_elements_synsets_2['Patient'] = wn.synset('affected_role.n.01')
    frame_elements_synsets_2['Event'] = wn.synset('event.n.01')
    frame_elements_synsets_2['Depictive'] = wn.synset('delineative.s.01')
    frame_elements_synsets_2['Result'] = wn.synset('consequence.n.01')
    frame_elements_synsets_2['Means'] = wn.synset('means.n.02')
    frame_elements_synsets_2['Manner'] = wn.synset('manner.n.01')
    frame_elements_synsets_2['Time'] = wn.synset('time.n.01')
    frame_elements_synsets_2['Place'] = wn.synset('place.n.02')
    frame_elements_synsets_2['Cause'] = wn.synset('cause.n.01')
    
    #LUs
    lexical_units_synsets_2 = dict()
    
    synsets_frame_2 = utils.SynsetsFrame(frame_id_2, frame_name_2, frame_synset_2, 
                                       frame_elements_synsets_2, lexical_units_synsets_2)
    
    synsets_frames_list_annotations.append(synsets_frame_2)
    
    
    #-------------------------------------------------------------#
    
    frame_id_3 = 2411
    frame_name_3 = "Personal_success"
    
    #Frame_name
    frame_synset_3 = wn.synset('success.n.02')
    
    #FEs
    frame_elements_synsets_3 = dict()
    frame_elements_synsets_3['Person'] = wn.synset('person.n.01')
    frame_elements_synsets_3['Time'] = wn.synset('time.n.02')
    frame_elements_synsets_3['Degree'] = wn.synset('degree.n.02')
    frame_elements_synsets_3['Endeavor'] = wn.synset('attempt.n.01')
    frame_elements_synsets_3['Explanation'] = wn.synset('explanation.n.01')
    frame_elements_synsets_3['Field'] = wn.synset('discipline.n.01')
    
    #LUs
    lexical_units_synsets_3 = dict()
    lexical_units_synsets_3['success [person].n'] = wn.synset('achiever.n.01')
    lexical_units_synsets_3['success [event].n'] = wn.synset('success.n.01')
    lexical_units_synsets_3['success [state].n'] = wn.synset('success.n.03')
    lexical_units_synsets_3['successful.a'] = wn.synset('successful.a.01')
    lexical_units_synsets_3['arrive.v'] = wn.synset('arrive.v.02')
    lexical_units_synsets_3['succeed.v'] = wn.synset('succeed.v.01')
    
    synsets_frame_3 = utils.SynsetsFrame(frame_id_3, frame_name_3, frame_synset_3, 
                                       frame_elements_synsets_3, lexical_units_synsets_3)
    
    synsets_frames_list_annotations.append(synsets_frame_3)
    
    
    #-------------------------------------------------------------#
    frame_id_4 = 1684
    frame_name_4 = 'Scrutinizing_for'
    
    #Frame_name
    frame_synset_4 = wn.synset('size_up.v.01')
    
    #FEs
    frame_elements_synsets_4 = dict()
    frame_elements_synsets_4['Ground'] = wn.synset('ground.n.08')
    frame_elements_synsets_4['Phenomenon'] = wn.synset('phenomenon.n.01')
    frame_elements_synsets_4['Manner'] = wn.synset('manner.n.01')
    frame_elements_synsets_4['Means'] = wn.synset('means.n.01')
    frame_elements_synsets_4['Degree'] = wn.synset('degree.n.02')
    frame_elements_synsets_4['Purpose'] = wn.synset('purpose.n.01')
    frame_elements_synsets_4['Instrument'] = wn.synset('instrumental_role.n.01')
    
    #LUs
    lexical_units_synsets_4 = dict()
    
    synsets_frame_4 = utils.SynsetsFrame(frame_id_4, frame_name_4, frame_synset_4, 
                                       frame_elements_synsets_4, lexical_units_synsets_4)
    
    synsets_frames_list_annotations.append(synsets_frame_4)
    
    
    #-------------------------------------------------------------#
    
    frame_id_5 = 2576
    frame_name_5 = 'Cache'
    
    #Frame_name
    frame_synset_5 = wn.synset('hoard.n.01')
    
    #FEs
    frame_elements_synsets_5 = dict()
    frame_elements_synsets_5['Cache'] = wn.synset('hoard.n.01')
    frame_elements_synsets_5['Resource'] = wn.synset('resource.n.01')
    frame_elements_synsets_5['Use'] = wn.synset('use.v.01')
    frame_elements_synsets_5['Possessor'] = wn.synset('owner.n.02')
    frame_elements_synsets_5['Descriptor'] = wn.synset('descriptor.n.02')
    
    #LUs
    lexical_units_synsets_5 = dict()
    lexical_units_synsets_5['cache.n'] = wn.synset('hoard.n.01')
    lexical_units_synsets_5['stash.n'] = wn.synset('hoard.n.01')
    
    synsets_frame_5 = utils.SynsetsFrame(frame_id_5, frame_name_5, frame_synset_5, 
                                       frame_elements_synsets_5, lexical_units_synsets_5)
    
    synsets_frames_list_annotations.append(synsets_frame_5)
    
    return synsets_frames_list_annotations




