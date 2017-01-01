# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 21:47:30 2016
@author: soma0sd
"""
from dbgen.modules import ensdf

cards = ensdf.card_all()
level = [i for i in cards if ensdf.B_card_levels(i)]

