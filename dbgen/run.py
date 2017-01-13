# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 21:47:30 2016
@author: soma0sd
"""
from dbgen.modules import ensdf
from dbgen.modules import path

import pickle


def step1():
  cards = ensdf.card_all()
  level = [ensdf.adopted_levels(i).levels for i in cards if ensdf.B_card_levels(i)]
  pickle.dump(level, open(path.path_step('step1.pkl'), 'wb'))
  return level


data = step1()