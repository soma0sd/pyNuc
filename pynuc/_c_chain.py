# -*- coding: utf-8 -*-
import pynuc as _nuc
import numpy as _np


class chain:
  def __init__(self, nucid, weights: float=1.0):
    self.C0 = _nuc.nuclide(nucid, weights)

  def decay_mixture(self):
    self._tmp = []
    self._decay_list(self.C0)
    return list(set(self._tmp))

  def decay(self, time):
    self._tmp = [[[self.C0._asc_code(), 100]]]
    self._chain_tree(self.C0._asc_code(), self._tmp[0])
    val = {}
    for tree in self._tmp:
      key = tree[-1][0]
      if key in val.keys():
        val[key] += self._bateman(time, tree)
      else:
        val[key] = self._bateman(time, tree)
    return val

  def activity(self, time):
    self._tmp = [[[self.C0._asc_code(), 100]]]
    self._chain_tree(self.C0._asc_code(), self._tmp[0])
    val = {}
    for tree in self._tmp:
      key = tree[-1][0]
      if key in val.keys():
        val[key] += self._bateman(time, tree)*_nuc.nuclide(key).info['T']
      else:
        val[key] = self._bateman(time, tree)*_nuc.nuclide(key).info['T']
    return val

  def _chain_tree(self, nucid, arr=[]):
    for mode in _nuc.nuclide(nucid).info['MODE']:
      e = _nuc.nuclide(mode[2])._asc_code()
      nar = arr+[[e, mode[1]]]
      self._tmp.append(nar)
      self._chain_tree(e, nar)

  def _bateman(self, time, tree):
    value = 0
    ratio = product([i[1]/100 for i in tree])
    lamb = [_nuc.nuclide(i[0]).info['T'] for i in tree]
    numer = product(lamb[:-1])*ratio
    for l in lamb:
      Cn = numer*_np.exp(-l*time)/denomi(lamb, l)
      value += Cn
    try:
      for iv, v in enumerate(value[1:]):
        if v <= 0:
          value[iv+1] = value[iv]
    except:
      pass
    return value

  def _decay_list(self, nuc, m = []):
    if len(nuc.info['MODE']):
      self._tmp += m
    for n in nuc.info['MODE']:
      e = _nuc.nuclide(n[2])
      m.append(e._asc_code())
      self._decay_list(e, m)


def product(arr):
  value = 1
  for v in arr:
    value *= v
  return value

def denomi(arr, lamb):
  value = 1
  for v in arr:
    if v == lamb:
      pass
    else:
      value *= v-lamb
  return value
