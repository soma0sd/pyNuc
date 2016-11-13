# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:34:18 2016
@author: soma0sd
"""
import ENSDF00 as ref
import re

rexa = re.compile(r'ADOPTED LEVELS')
rexb = re.compile(r'^([ \d]{2}\d\w[ \w])')

fpath = ref.ENSDF_paths()
cards = []
nucid = []
for p in fpath:
  with open(p, 'r') as f:
    sub = []
    for l in f.readlines():
      if l.strip() == '':
        m = rexb.match(sub[0])
        if m:
          if not m.group(0) in nucid:
            nucid.append(m.group(0))
        cards.append(sub)
        sub = []
      else:
        sub.append(l.strip('\n'))
del fpath, p, l, sub

sub = []
for c in cards:
  m = rexa.findall(c[0])
  if m:
    sub.append(c)
cards = sub
del sub, c, m

counter = []
cont = {}
for i in cards:
  m = rexb.match(i[0])
  if m.group(0) in counter:
    print(cont[m.group(0)])
    print(i[0])
  else:
    counter.append([m.group(0)])
    cont[m.group(0)] = i[0]
print(len(counter))
del i, counter, cont

