# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:53:53 2016
@author: soma0sd
"""
import matplotlib.pyplot as plt
import re

rexa = re.compile(r'^235U  {4}ADOPTED LEVELS')
rexb = re.compile(r'^235U   L')

cards = []
with open('ensdf/ensdf_151208_294/ensdf.235', 'r') as f:
  card = []
  for i in f.readlines():
    if i.strip() == '':
      cards.append(card)
      card = []
    else:
      card.append(i.strip('\n'))

for i in cards:
  m = rexa.match(i[0])
  if m:
    card = i

cards = []
sub = []
for i in card:
  m = rexb.match(i)
  if m:
    cards.append(sub)
    sub = [i]
  else:
    sub.append(i)

fig = plt.figure()
ax = fig.add_subplot(111)
for i in cards[1:]:
  lv = float(i[0][9:19])
  ax.plot([1,10], [lv, lv], '-k')
ax.set_ylabel('Energy [keV]')
del i, sub, lv
