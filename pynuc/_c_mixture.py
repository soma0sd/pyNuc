# -*- coding: utf-8 -*-
import pynuc as _pn

class mixture:
  def __init__(self, mixture=[]):
    self.mixture = mixture

  def element_del(self, ix):
    del self.mixture[ix]

  def element_append(self, nucid, N):
    code = _pn.nuclide(nucid)._asc_code()
    self.mixture.append(code)

  def get_elements(self):
    return self.mixture
