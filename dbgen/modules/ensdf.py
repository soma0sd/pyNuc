# -*- coding: utf-8 -*-
from dbgen.modules import path as _path

import re as _re


"""
module initialization functions
"""
def _get_nucid_zz():
  data = {}
  path = _path.path_reference('ensdf_nucid_zz.csv')
  for l in open(path, 'r').readlines():
    l = l.replace('\n', '')
    item = l.split(',')
    data[item[0]] = int(item[1])
  return data

def _get_decay_delta():
  data = {}
  path = _path.path_reference('ensdf_decay_delta.csv')
  for l in open(path, 'r').readlines():
    l = l.replace('\n', '')
    item = l.split(',')
    data[item[0].strip()] = {'dZ': int(item[1]), 'dA': int(item[2])}
  return data

_trans_zz = _get_nucid_zz()
_decay_product = _get_decay_delta()


"""
basic ENSDF functions
"""
def card_all():
  data = []
  file = _path.file_ensdf()
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


"""
card analysis class
"""
class adopted_levels:
  _rgex0 = _re.compile(r"""
    .{5}[ ]{2}L[ ]{1}                 # LEVEL RECORD
    (?P<E>[\d. E]{10})(?P<DE>.{2})
    (?P<J>.{18})
    (?P<T>.{10})(?P<DT>.{6})
    (?P<L>.{9})
    (?P<S>.{10})(?P<DS>.{2})
    (?P<MS>.{3})
    """, _re.VERBOSE)
  _rgex1 = _re.compile(r"""
    .{5}[ ]{2}G[ ]{1}                 # GAMMA RECORD
    (?P<E>[\d. E]{10})(?P<DE>.{2})
    (?P<RI>.{8})(?P<DRI>.{2})
    (?P<M>.{10})
    (?P<MR>.{8})(?P<DMR>.{6})
    (?P<CC>.{7})(?P<DCC>.{2})
    (?P<TI>.{9})(?P<DTI>.{2})
    (?P<C>.)(?P<COIN>.)
    """, _re.VERBOSE)
  _rgex2 = _re.compile(r"""
    (?P<MODE>%.+?)                    # Decay Mode 1
    [=<>~]
    (?P<VAL>[\d\.E-]+)
    """, _re.VERBOSE)
  _rgex3 = _re.compile(r"""
    (?P<MODE>%.+?)                    # Decay Mode 2
    [ ][A-Z]{2}[ ]
    (?P<VAL>[\d\.E-]+)
    """, _re.VERBOSE)

  def __init__(self, card: list):
    self.key = nucid2dbkey(card[0][:5])
    self._level_raw = []
    self.levels = []
    data = []
    for l in card:
      m = self._rgex0.match(l)
      if m:
        if len(data) > 1:
          self._level_raw.append(data)
        data = [l]
      elif l[6] != 'C' and l[6] != 'c' :
        data.append(l)
    self._level_raw.append(data)
    del self._level_raw[0]
    self._level_split(self._level_raw)

  def __ans_T(self, data, s):
    item = s.strip().split(' ')
    if len(item) > 1:
      if item[1] in ['MEV', 'KEV', 'EV']:
        data['T'] = 0
      else:
        data['T']  = item[0]
        data['TU'] = item[1]
    else:
      data['T'] = 0

  def __ans_G(self, data, desc):
    riregx = _re.compile('([\d\.]+)')
    for l in desc[1:]:
      g = self._rgex1.match(l)
      if g:
        ri = riregx.match(g.group('RI').strip())
        if not ri:
          ri = 100
        else:
          ri = float(ri.group(1))
        data['GE'].append([float(g.group('E')), ri])

  def __ans_J(self, J):
    ...

  def __ans_decay(self, data, desc):
    DM = []
    for l in desc[1:]:
      m1 = self._rgex2.findall(l)
      m2 = self._rgex3.findall(l)
      if m1:
        DM += self.__ans_decay_product(m1)
      if m2:
        DM += self.__ans_decay_product(m2)
    data['DM'] = DM

  def __ans_decay_product(self, mode):
    data = []
    for br in mode:
      if 'IT' in br[0]:
        data.append(list(br))
      elif 'SF' in br[0]:
        continue
      elif br[0] not in _decay_product.keys():
        continue
      else:
        dA = _decay_product[br[0]]['dA']
        dZ = _decay_product[br[0]]['dZ']
        Z, A = int(self.key[:3]), int(self.key[3:])
        cord = "{:03d}{:03d}0000".format(Z+dZ, A+dA)
        data.append(list(br)+[cord])
    return data

  def __ans_decay_branchs(self, brs: list):
    ...

  def _level_split(self, raw: list):
    for m, lv in enumerate(raw):
      l = self._rgex0.match(lv[0])
      data = {'E': 0, 'J': 0, 'T': 0, 'TU': 0, 'GE': []}
      key = self.key+"{:04d}".format(m)
      data['E'] = float(l.group('E'))
      data['J'] = l.group('J').strip()
      self.__ans_T(data, l.group('T'))
      self.__ans_G(data, lv)
      self.__ans_decay(data, lv)
      self.__ans_decay(data, lv)
      self.levels.append([key, data])

  def _get_level_info(self, level: list):
    ...
