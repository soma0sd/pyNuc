# -*- coding: utf-8 -*-
import pynuc as _nuc
import numpy as _np


class chain:
  def __init__(self, nuc):
    self.N0 = nuc

  def decay_mixture(self):
    return decay_list(self.N0)

def decay_list(nuc, m=[]):
  print(nuc.info['MODE'])
  if not nuc.info['MODE']:
    return m
  for n in nuc.info['MODE']:
      e = _nuc.nuclide(n[2])
      m.append(e)
      decay_list(e, m)
