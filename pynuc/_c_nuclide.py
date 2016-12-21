# -*- coding: utf-8 -*-s
import pynuc as _nuc
import numpy as _np


class nuclide:
  def __init__(self, nucid: str, weights: float=1.0):
    import re
    type1 = re.compile('(\d{3})(\d{3})').match(nucid)
    type2 = re.compile('(\d{1,3})([A-z][a-z]{0,2})').match(nucid)
    if type1:
      if nucid in _nuc.data_nuc.keys():
        self.info = _nuc.data_nuc[nucid]
      else:
        raise NuclideError(str(nucid)+" is not exist ENSDF DB")
    elif type2:
      A = int(type2.group(1))
      Z = serch_s2z(type2.group(2))
      nucid = "{:03d}{:03d}".format(Z, A)
      if nucid in _nuc.data_nuc.keys():
        self.info = _nuc.data_nuc[nucid]
      else:
        raise NuclideError(str(nucid)+" is not exist ENSDF DB")
    self.Z, self.A = int(nucid[:3]), int(nucid[3:])
    self.N0 = weights

  def decay(self, time):
    lamb = self.info['T']
    return _np.exp(-lamb*time)

  def get_chain(self):
    return _nuc.chain(self)

  def _asc_code(self):
    return str(self.A)+serch_z2s(self.Z)

  def __repr__(self):
    dm = self.info['MODE']
    pr = ' '+self._asc_code()+' '+'='*25+'\n'
    pr += 'halflife: '+'{:.4E} sec'.format(_np.log(2)/self.info['T'])+'\n'
    if len(dm) == 1:
      e = nuclide(dm[0][2])
      pr += 'Decay: '+dm[0][0]+', {}'.format(dm[0][1])+', '+e._asc_code()+'\n'
    elif len(dm) > 1:
      e = nuclide(dm[0][2])
      pr += 'Decay: '+dm[0][0]+', {}'.format(dm[0][1])+', '+e._asc_code()+'\n'
      for m in dm[1:]:
        e = nuclide(m[2])
        pr += '       '+m[0]+', {}'.format(m[1])+', '+e._asc_code()+'\n'
    else:
      pr += 'stable'
    return pr


class NuclideError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def serch_s2z(sym):
  Z = -1
  for key in _nuc.data_nist.keys():
    if sym == _nuc.data_nist[key]['SYM']:
      Z = int(key[:3])
      break
  if Z == -1:
    raise NuclideError('Symbol '+sym+' not exist')
  return Z


def serch_z2s(Z: int):
  sym = ''
  for key in _nuc.data_nist.keys():
    if '{:03d}'.format(Z) == key[:3]:
      sym = _nuc.data_nist[key]['SYM']
      break
  if sym == '':
    raise NuclideError('Symbol '+sym+' not exist')
  return sym
