# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 22:15:57 2016
@author: soma0sd
@Nucid \d{3}\w{2} [AAASS] => \d{3}\d{3} [AAAZZZ]
"""
import re
import os
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


tr = {'NN': 0, 'H ': 1, 'HE': 2, 'LI': 3, 'BE': 4, 'B ': 5, 'C ': 6, 'N ': 7, 'O ': 8, 'F ': 9, 'NE': 10, 'NA': 11, 'MG': 12, 'AL': 13, 'SI': 14, 'P ': 15, 'S ': 16, 'CL': 17, 'AR': 18, 'K ': 19, 'CA': 20, 'SC': 21, 'TI': 22, 'V ': 23, 'CR': 24, 'MN': 25, 'FE': 26, 'CO': 27, 'NI': 28, 'CU': 29, 'ZN': 30, 'GA': 31, 'GE': 32, 'AS': 33, 'SE': 34, 'BR': 35, 'KR': 36, 'RB': 37, 'SR': 38, 'Y ': 39, 'ZR': 40, 'NB': 41, 'MO': 42, 'TC': 43, 'RU': 44, 'RH': 45, 'PD': 46, 'AG': 47, 'CD': 48, 'IN': 49, 'SN': 50, 'SB': 51, 'TE': 52, 'I ': 53, 'XE': 54, 'CS': 55, 'BA': 56, 'LA': 57, 'CE': 58, 'PR': 59, 'ND': 60, 'PM': 61, 'SM': 62, 'EU': 63, 'GD': 64, 'TB': 65, 'Dy': 66, 'DY': 66, 'HO': 67, 'ER': 68, 'TM': 69, 'YB': 70, 'LU': 71, 'HF': 72, 'TA': 73, 'W ': 74, 'RE': 75, 'OS': 76, 'IR': 77, 'PT': 78, 'AU': 79, 'HG': 80, 'TL': 81, 'PB': 82, 'BI': 83, 'PO': 84, 'AT': 85, 'RN': 86, 'FR': 87, 'RA': 88, 'AC': 89, 'TH': 90, 'PA': 91, 'U ': 92, 'NP': 93, 'PU': 94, 'AM': 95, 'CM': 96, 'BK': 97, 'CF': 98, 'ES': 99, 'FM': 100, 'MD': 101, 'NO': 102, 'LR': 103, 'RF': 104, 'DB': 105, 'SG': 106, 'BH': 107, 'HS': 108, 'MT': 109, '10': 110, 'DS': 110, 'RG': 111, 'CN': 112, '12': 112, '13': 113, '14': 114, 'FL': 114, '15': 115, '16': 116, '17': 117, '18': 118}

fpath = []
drRoot = os.path.join(os.path.dirname(__file__),'ensdf')
drList = os.listdir(drRoot)

for dr1 in drList:
  uRoot = os.path.join(drRoot, dr1)
  for dr2 in os.listdir(uRoot):
    fpath.append(os.path.join(uRoot, dr2))
del dr1, dr2, drList, drRoot, uRoot

rexA = re.compile(r'^(?P<A>[ \d]{2}\d)(?P<S>\w[ \w])   ')

data = {i: [] for i in range(1, 295)}
for p in fpath:
  with open(p, 'r') as f:
    for l in f.readlines():
      m = rexA.match(l)
      if m:
        print('\r {}'.format(l), end='')
        data[int(m.group('A'))] += [tr[m.group('S')]]
del fpath, l, p

for k in data.keys():
  data[k] = list(set(data[k]))


fig = plt.figure()
ax = fig.add_subplot(111)

code = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
for x in data.keys():
  for y in data[x]:
    vect = [(x, y), (x, y+1), (x+1, y+1), (x+1, y), (x, y)]
    patch = patches.PathPatch(Path(vect, code), facecolor='black', lw=2)
    ax.add_patch(patch)

ax.set_xlim(1,300)
ax.set_ylim(0,120)
ax.set_xlabel('Mass Number')
ax.set_ylabel('Atomic Number')
plt.show()
