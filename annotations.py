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
	ID:   10      frame: Transitive_action
	ID: 2411    	  frame: Personal_success
	ID: 1684    	  frame: Scrutinizing_for
	ID: 2576	      frame: Cache
"""

#-------------------------------------------------------------#


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



#LUs
lexical_units_synsets_2 = dict()

#-------------------------------------------------------------#


#-------------------------------------------------------------#


#-------------------------------------------------------------#


#-------------------------------------------------------------#




