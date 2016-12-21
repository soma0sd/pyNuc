# -*- coding: utf-8 -*-


def _get_ensdf_symbols():
  from ensdf import genlib
  from os import path
  data = {}
  dr = path.abspath(path.join(path.abspath(genlib.__file__), '..'))
  fname = 'nucid2z.csv'
  f = open(path.join(dr,fname))
  for l in f.readlines():
    item = l.split(',')
    data[item[0]] = int(item[1])
  return data


def nucid2nucpy(nucid:str):
  nucid_z = _get_ensdf_symbols()
  A = int(nucid[:3])
  Z = nucid_z[nucid[3:]]
  return "{:03d}{:03d}".format(Z, A)


_nucid = '(?P<NUCID>[ \d]{2}\d\w[ \w])'
_e     = '(?P<E>.{10})(?P<DE>.{2})'
_j     = '(?P<J>.{18})'
_t     = '(?P<T>.{10})(?P<DT>.{6})'
_l     = '(?P<L>.{9})'
_s     = '(?P<S>.{10})(?P<DS>.{2})'
_c     = '(?P<C>.)'
_ms    = '(?P<MS>.{3})'
_dm    = '(?P<MODS>%.+)'

def re_level_rec(l):
  import re
  rex = re.compile(_nucid+'  L '+_e+_j+_t+_l+_s+_c+_ms)
  m = rex.match(l)
  if not m:
    return None
  else:
    data = {}
    data['NUCID'] = m.group('NUCID')
    data['E'] = _rec_E(m.group('E').strip('# '))
    data['J'] = m.group('J').strip('# ')
    data['T'] = _rec_T(m.group('T').strip('# '))
    return data


def _rec_E(E):
  import re
  rex = re.compile('([\d.]+)')
  m = rex.match(E)
  if m:
    return float(m.group(0))
  else:
    return -1.0


def _rec_T(T):
  import numpy as np
  if T in ['STABLE', '']:
    return 0
  T = T.split(' ')
  if len(T) < 2:
    print(T, 'no parsor')
    return -1.0
  elif T[1] in ['MEV', 'KEV', 'EV']:
    return -1.0
  unit = {'S': 1, 'M': 60, 'H': 3600, 'D': 86400, 'Y': 31556926}
  unit.update({'MS': 1E-3, 'US': 1E-6, 'NS': 1E-9, 'PS': 1E-12})
  unit.update({'FS': 1E-15, 'AS': 1E-18})
  return np.log(2)/(float(T[0])*unit[T[1]])


def re_level_decay(m):
  import re
  rex = re.compile(_nucid+'\d L '+_dm)
  m = rex.match(m)
  if not m:
    return None
  elif '%' not in m.group('MODS'):
    return None
  else:
    data = m.group('MODS').strip()
    return data

def mode_parsing(mods, key):
  import re
  rex = re.compile('(\(.+\))')
  rm = rex.findall(mods)
  if rm:
    mods = mods.replace(rm[0], '')
  data = []
  for m in mods.split('$'):
    m = m.strip()
    if m == '':
      pass
    if '%' not in m:
      pass
    elif '?' in m:
      pass
    else:
      branch = _branch_pasing(m)
      if len(branch) > 1:
        data.append(branch)
  data = _branch_normalization(data)
  data = _decay_product(data, key)
  return data

def _branch_pasing(branch):
  import re
  data = []
  rex1 = re.compile('(?P<MODE>%.+?)[=<>~](?P<VAL>[\d\.E-]+)')
  rex2 = re.compile('(?P<MODE>%.+?) [A-Z]{2} (?P<VAL>[\d\.E-]+)')
  m1 = rex1.match(branch)
  m2 = rex2.match(branch)
  if m1:
    data = [m1.group('MODE'), float(m1.group('VAL'))]
  elif m2:
    data =  [m2.group('MODE'), float(m2.group('VAL'))]
  else:
    return []
  if data[0] in ['%SF', '%|b{+-}fission']:
    return []
  return data

def _branch_normalization(mode):
  if len(mode) < 2:
    return mode
  if '%B-' in mode[0][0]:
    dl = 0
    for m in mode[1:]:
      if '%B-' in m[0]:
        dl += m[1]
    mode[0][1] -= dl
  if '%EC' in mode[0][0]:
    dl = 0
    for m in mode[1:]:
      if '%EC' in m[0]:
        dl += m[1]
    mode[0][1] -= dl
  if '%B+' in mode[0][0]:
    dl = 0
    for m in mode[1:]:
      if '%B+' in m[0]:
        dl += m[1]
    mode[0][1] -= dl
  if mode == [['%2P', 100.0], ['%A', 100.0]]:
    return [['%A', 100.0]]
  if 100 < sum([i[1] for i in mode]) < 150:
    s = sum([i[1] for i in mode])
    for m in mode:
      m[1] = m[1]*100/s
  return mode

def _decay_product(mode, key):
  import re
  data = []
  rex1 = re.compile('(%.+)')
  rex2 = re.compile('(%.+?)[+](%.+)')
  rex3 = re.compile('(%.+?)[+](%.+?)[+](%.+)')
  Z, A= int(key[:3]), int(key[3:])
  for m in mode:
    m1 = rex1.match(m[0])
    m2 = rex2.match(m[0])
    m3 = rex3.match(m[0])
    dZ, dA = 0, 0
    x = 0
    if m3:
      for i in m3.groups():
        _Z, _A = _prod_decay(i)
        dZ += _Z
        dA += _A
    elif m2:
      for i in m2.groups():
        _Z, _A = _prod_decay(i)
        dZ += _Z
        dA += _A
    elif m1:
      try:
        for i in m1.groups():
          _Z, _A = _prod_decay(i)
          if _Z is None:
            x = 1
          dZ += _Z
          dA += _A
      except:
        print(key, m)
    code = "{:03d}{:03d}".format(Z+dZ, A+dA)
    if x == 0:
      data.append([m[0], m[1], code])
  return data


_dZ = {'%SF': 0, '%A': -2, '%EC': -1, '%B-': 1, '%B+': -1, '%ECP': -2}
_dA = {'%SF': 0, '%A': -4, '%EC': 0,  '%B-': 0, '%B+': 0,  '%ECP': -1}
_dZ.update({'%EC2P': -3, '%34SI': -14, '%ECSF': -1, '%ECF': -1, '%B-F': 1})
_dA.update({'%EC2P': -2, '%34SI': -34, '%ECSF': 0, '%ECF': 0,  '%B-F': 0})
_dZ.update({'%14C': -6,  '%B-N': 1,  '%P': -1, '%ECA': -2, '%B+P': -1})
_dA.update({'%14C': -14, '%B-N': -1, '%P': -1, '%ECA': -1, '%B+P': -2})
_dZ.update({'%2B-': -2, '%B+A': -3, '%12C': -6,  '%B-2N': 1,  '%2P': -2})
_dA.update({'%2B-': 0,  '%B+A': -4, '%12C': -12, '%B-2N': -2, '%2P': -2})
_dZ.update({'%B+2P': -3, '%2N': 0,  '%N': 0,  '%B-3N': 1,  '%B-A': -1})
_dA.update({'%B+2P': 2,  '%2N': -2, '%N': -1, '%B-3N': -3, '%B-A': -4})
_dZ.update({'%B-4N': 1})
_dA.update({'%B-4N': -4})

_dZ['%{+34}Si'] = _dA['%{+34}Si'] = _dZ['%{+20}Ne'] = _dA['%{+20}Ne'] = None
_dZ['%Ne'] = _dA['%Ne'] = _dZ['%{+24}Ne'] = _dA['%{+24}Ne'] = None
_dZ['%{+25}Ne'] = _dA['%{+25}Ne'] = _dZ['%Mg'] = _dA['%Mg'] = None
_dZ['%{+28}Mg'] = _dA['%{+28}Mg'] = _dZ['%{+22}Ne'] = _dA['%{+22}Ne'] = None
_dZ['%2|e'] = _dA['%2|e'] = None

def _prod_decay(mode):
  dZ, dA = _dZ, _dA
  return dZ[mode], dA[mode]

