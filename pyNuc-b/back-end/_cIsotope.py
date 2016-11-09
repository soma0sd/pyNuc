# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 00:06:33 2016
@author: soma0sd
"""
from pyNuc.core import GetElementSymbol

d = GetElementSymbol()

class isotope:
  def __init__(self, *arg):
    ...

  def config(self, **kw):
    ...

class finder:
  def __init__(self):
    ...

  def GetIsotopes(self):
    ...

class mixture:
  def __init__(self, *elems):
    self.Elements = list(elems)

  def GetIsotopes(self):
    ...
