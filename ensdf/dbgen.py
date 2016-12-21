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
        data[key]['MODE'] = []
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


def get_nist():
  import re
  data = {}
  iso = []
  card = []
  re_C = re.compile('^[_]+$')
  re_i = re.compile('^(.{3}) (.{3}) (.{3})  (.{1,18})[ ]*(.{0,13})')
  re_f = re.compile('[\d\.]+')
  f = files.get_nist_file()
  for l in f.readlines()[3:]:
    l = l.replace('\n', '')
    if re_C.match(l):
      iso.append(card)
      card = []
    else:
      card.append(l)
  for c in iso:
    m1 = re_i.match(c[0])
    main = m1.groups()
    Z = int(main[0])
    symbol = main[1].strip()
    mass = float(re_f.match(main[3]).group(0))
    if re_f.match(main[4]):
      na = float(re_f.match(main[4]).group(0))
    else:
      na = 0.0
    code = "{:03d}{:03d}".format(Z, int(main[2]))
    data[code] = {'SYM': symbol, 'M': mass, 'IS': na}
    for cs in c[1:]:
      m2 = re_i.match(cs)
      sub = m2.groups()
      mass = float(re_f.match(sub[3]).group(0))
      if re_f.match(sub[4]):
        na = float(re_f.match(sub[4]).group(0))
      else:
        na = 0.0
      code = "{:03d}{:03d}".format(Z, int(sub[2]))
      data[code] = {'SYM': symbol, 'M': mass, 'IS': na}
  data['000001'] = {'SYM': 'n', 'M': 1.008664916, 'IS': 0.0}
  return data

data = 0
data = get_ground_level()
nist = get_nist()
f = open('nucinfo.pkl', 'wb')
pickle.dump(data, f)
f = open('nist.pkl', 'wb')
pickle.dump(nist, f)
