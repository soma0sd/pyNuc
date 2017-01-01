# -*- coding: utf-8 -*-
from dbgen.modules import file as _file

import re as _re


def _nucid_zz():
  data = {}
  path = _file.path_reference('ensdf_nucid_zz.csv')
  for l in open(path, 'r').readlines():
    l = l.replace('\n', '')
    item = l.split(',')
    data[item[0]] = int(item[1])
  return data

try:
  _trans_zz
except:
  _trans_zz = _nucid_zz()

def card_all():
  data = []
  file = _file.file_ensdf()
  for f in file:
    card = []
    for l in f.readlines():
      l = l.replace('\n', '')
      if l.strip() == '':
        data.append(card)
        card = []
      else:
        card.append(l)
  return data


def B_card_levels(card):
  return "ADOPTED LEVELS" in card[0]


def nucid2dbkey(nucid):
  return "{:03d}{:03d}".format(_trans_zz[nucid[3:]], int(nucid[:3]))
