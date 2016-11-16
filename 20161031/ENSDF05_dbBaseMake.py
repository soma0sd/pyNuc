# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 22:34:25 2016
@author: soma0sd

data['key'] = [isotopes data keywords]
data['range'] = {'AAA': [Z range]}
data['data'] = {'AAAZZZ': {'key': isotopes data}}
"""
import ENSDF00 as ref
import re

tSymb = ref.trans_symbol()
fPath = ref.ENSDF_paths()
rexa = re.compile(r'^(?P<A>[ \d]{2}\d)(?P<S>\w[ \w])')

data = {}
data['key'] = []
data['range'] = {}
data['data'] = {}

"""
Make Document
"""
docs = []
for p in fPath:
  card = []
  with open(p) as f:
    for l in f.readlines():
      if l.strip() == '':
        docs.append(card)
        card = []
      else:
        card.append(l)
del p, l, card, fPath
"""
Data input
"""
for d in docs:
  m = rexa.match(d[0])
  if m:
    A = int(m.group('A').strip())
    Z = tSymb[m.group('S')]
    try:
      data['range'][A] += [Z]
    except:
      data['range'][A] = [Z]
    code = "{:03d}{:03d}".format(A, Z)
    data['data'][code] = {}
"""Range set"""
for d in data['range'].keys():
  data['range'][d] = list(set(data['range'][d]))
del d, A, Z, code, docs, tSymb
