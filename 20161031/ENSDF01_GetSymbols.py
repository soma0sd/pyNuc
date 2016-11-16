# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 18:16:45 2016
@author: soma0sd

@ Output: 20151210 Data, run 20161106

{'NN': 0, 'H ': 1, 'HE': 2, 'LI': 3, 'BE': 4, 'B ': 5, 'C ': 6, 'N ': 7, 'O ': 8, 'F ': 9, 'NE': 10, 'NA': 11, 'MG': 12, 'AL': 13, 'SI': 14, 'P ': 15, 'S ': 16, 'AR': 18, 'CL': 17, 'K ': 19, 'CA': 20, 'SC': 21, 'TI': 22, 'V ': 23, 'CR': 24, 'MN': 25, 'FE': 26, 'CO': 27, 'NI': 28, 'CU': 29, 'ZN': 30, 'GA': 31, 'GE': 32, 'AS': 33, 'SE': 34, 'BR': 35, 'KR': 36, 'RB': 37, 'SR': 38, 'Y ': 39, 'ZR': 40, 'NB': 41, 'MO': 42, 'TC': 43, 'RU': 44, 'RH': 45, 'PD': 46, 'AG': 47, 'CD': 48, 'IN': 49, 'OS': 76, 'IR': 77, 'PT': 78, 'AU': 79, 'HG': 80, 'TL': 81, 'PB': 82, 'BI': 83, 'PO': 84, 'AT': 85, 'RN': 86, 'FR': 87, 'RA': 88, 'AC': 89, 'TH': 90, 'PA': 91, 'U ': 92, 'NP': 93, 'PU': 94, 'AM': 95, 'CM': 96, 'BK': 97, 'CF': 98, 'ES': 99, 'FM': 100, 'MD': 101, 'NO': 102, 'LR': 103, 'RF': 104, 'DB': 105, 'SG': 106, 'BH': 107, 'HS': 108, 'MT': 109, '10': 110, 'DS': 110, 'RG': 111, '12': 112, '13': 113, 'CN': 112, 'FL': 114, '14': 114, '15': 115, '16': 116, '17': 117, '18': 118}
"""
import os
import re


drRoot = os.path.join(os.path.dirname(__file__).replace('20161031', ''),'ensdf')
drList = os.listdir(drRoot)
rexA = re.compile(r'^(?P<nucid>[ \d]{2}\d\w[ \w]) ')

data = []
for dr1 in drList:
  uRoot = os.path.join(drRoot, dr1)
  for dr2 in os.listdir(uRoot):
    fPath = os.path.join(uRoot, dr2)
    with open(fPath, 'r') as f:
      for l in f.readlines():
        m = rexA.search(l)
        if m:
          if not m.group('nucid') in data:
            data.append(m.group('nucid'))

print("=== ENSDF Status ===\n")
print("  {: 4d} Istopes".format(len(data)))

syms = []
for s in data:
  sym = s[3:5]
  if not sym in syms:
    syms.append(sym)

print('  {: 4d} Symbols'.format(len(syms)))
print('{',end='')
for s in syms:
  print('\'{}\''.format(s),end=': , ')
print('}')