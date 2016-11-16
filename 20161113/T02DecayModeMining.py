# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 02:45:44 2016
@author: soma0sd
"""
import ENSDF as sub
import re

rexa = re.compile(r'%[\w{][^ $]*?[=<>]')
rexb = re.compile(r'%[\w{][^ $]*? AP ')
rexc = re.compile(r'%[\w{][^ $]*? LE ')
rexd = re.compile(r'%[\w{][^ $]*? GT ')
rexe = re.compile(r'%[\w{][^ $]*? LT ')

LvCard = sub.get_level_card()
LvLine = []
Debug = []
data = []
out = []
for card in LvCard:
  for line in card:
    if line[9] is '%':
      LvLine.append(line[9:])
      m1 = rexa.findall(line)
      m2 = rexb.findall(line)
      m3 = rexc.findall(line)
      m4 = rexd.findall(line)
      m5 = rexe.findall(line)
      if m1 or m2 or m3 or m4 or m5:
        for item in m1:
          data.append(item.strip('=<>'))
        for item in m2:
          data.append(item.replace(' AP ', ''))
        for item in m3:
          data.append(item.replace(' LE ', ''))
        for item in m4:
          data.append(item.replace(' GT ', ''))
        for item in m5:
          data.append(item.replace(' LT ', ''))
      else:
        out.append(line)
del LvCard, card, line, m1, m2, m3, m4, m5, item

for line in LvLine:
  d = line
  for item in data:
    d = d.replace(item, '')
  if '%' in d:
    Debug.append(d)
del d, item, line, LvLine

data = list(set(data))
for d in data:
  print(d, end=', ')
del d
print()

