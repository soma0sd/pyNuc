# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 18:55:11 2016
@author: soma0sd
Create zero energy decay mode
"""
import ENSDF as sub
import re

Cards = sub.get_level_card()
rexa = re.compile('[ \w]{5}  L ')
rexb = re.compile('[ \w]{6} L %')

raw = []
for card in Cards:
  lv = []
  for l in card:
    m1 = rexa.match(l)
    m2 = rexb.match(l)
    if m1:
      if len(lv) > 0:
        raw += [lv]
      lv = [l]
    if m2:
      lv += [l]
      print(l)
del Cards, card, l
