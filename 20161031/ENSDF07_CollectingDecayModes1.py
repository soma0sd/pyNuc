# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 01:22:52 2016
@author: soma0sd
"""
import ENSDF00 as ref
import re

trcode = ref.trans_symbol()
fpath = ref.ENSDF_paths()
levels = []
for p in fpath:
  with open(p, 'r') as f:
    sub = []
    for l in f.readlines():
      if l.strip() == '':
        if 'ADOPTED LEVELS' in sub[0]:
          levels.append(sub)
        sub = []
      else:
        sub.append(l.strip('\n'))
del fpath, l, p, sub

rexa = re.compile(r'^[ \w]{5}\d L ')
rexb = re.compile(r'%[-+{}\w]+')

modes = []
for lv in levels:
  A, Z = int(lv[0][:3]), trcode[lv[0][3:5]]
  code = "{:03d}{:03d}".format(A, Z)
  for l in lv[1:]:
    ma = rexa.match(l)
    if ma and '%' in l:
      mb = rexb.findall(l)
      modes += [i for i in mb if not i in modes]
del A, Z, lv, trcode, code, l, mb, levels

for i in modes:
  print(i, end=', ')
del i
