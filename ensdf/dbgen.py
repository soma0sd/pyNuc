# -*- coding: utf-8 -*-
"""Inner Module Import"""
from ensdf.genlib import files
from ensdf.genlib import regexp

"""Python Packages"""
import pickle

def get_card(ident=''):
  data = []
  file_list = files.get_all_files()
  prog = lambda i: (i+1)*100/len(file_list)
  for ix, f in enumerate(file_list):
    card = []
    for l in f.readlines():
      l = l.replace('\n', '')
      if l.strip() == '':
        if ident in card[0]:
          data.append(card)
        card = []
      else:
        card.append(l)
    print("\rGet Card...        [{:6.2f}%]".format(prog(ix)), end='')
  print()
  return data

uq = []
def get_ground_level():
  global uq
  card = get_card("ADOPTED LEVELS")
  prog = lambda i: (i+1)*100/len(card)
  data = {}
  for ic, c in enumerate(card):
    for ixl, l1 in enumerate(c):
      lv = regexp.re_level_rec(l1)
      if lv:
        key = regexp.nucid2nucpy(lv['NUCID'])
        if key in data.keys():
          break
        data[key] = {}
        data[key]['E'] = lv['E']
        data[key]['J'] = lv['J']
        data[key]['T'] = lv['T']
        mods = ''
        for l2 in c[ixl+1:]:
          de = regexp.re_level_decay(l2)
          if regexp.re_level_rec(l2):
            break
          elif de:
            mods += de
            mode = regexp.mode_parsing(mods, key)
            data[key]['MODE'] = mode
    print("\rGet Ground level...[{:6.2f}%]".format(prog(ic)), end='')
  print()
  return data

data = get_ground_level()
f = open('nucinfo.pkl', 'wb')
pickle.dump(data, f)