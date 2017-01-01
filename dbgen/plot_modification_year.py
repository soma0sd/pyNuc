# -*- coding: utf-8 -*-
from dbgen.modules import ensdf
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

cards = ensdf.card_all()
level = [i for i in cards if ensdf.B_card_levels(i)]

plt.figure(figsize=(20, 8))
for _c in level:
  _nucid = _c[0][:5]
  _key = ensdf.nucid2dbkey(_nucid)
  if _c[0][74:79].strip() == '':
    plt.plot(int(_key[3:]), int(_key[:3]), 's', ms=3, lw=0)
    continue
  years = int(_c[0][74:78])
  _x, _y = int(_key[3:]), int(_key[:3])
  if years >= 2015:
    plt.plot(_x, _y, 's', ms=3, lw=0, color = '#ff0000')
  elif years >= 2005:
    plt.plot(_x, _y, 's', ms=3, lw=0, color = '#ff8800')
  else:
    plt.plot(_x, _y, 'ys', ms=3, lw=0)
p1 = mpatches.Patch(color='#ff0000', label='>2015')
p2 = mpatches.Patch(color='#ff8800', label='>2005')
p3 = mpatches.Patch(color='#ffff00', label='<2005')
plt.xlabel('Mass Number', fontsize=16)
plt.ylabel('Atomic Number', fontsize=16)
plt.legend(handles=[p1, p2, p3], loc=2, prop={'size':15},
           bbox_to_anchor=[0, 1], shadow=True, fancybox=True)
plt.grid()
plt.show()
