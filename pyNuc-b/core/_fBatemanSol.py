# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:35:36 2016
@author: soma0sd
"""
import numpy as np

class BatemanSol:
  def __init__(self, **kw):
    self.var = {'dc': [],    # Decay Constant
                'ratio': 1,  # isotopes population ratio
                'tmp': None }
    self.var.update(kw)
    if len(self.var['dc']) < 1:
      raise("decay constant error")

  def Concentration(self, time, ratio=None):  # float or linspace or logspace
    pop = 0
    dcs = self.var['dc']
    if ratio is None:
      ratio = self.var['ratio']
    n = np.prod(np.array([i for i in dcs[:-1]]))*ratio
    for i in dcs:
      m = np.prod(np.array([d-i for d in dcs if not d-i == 0]))
      pop += n*np.exp(-i*time)/m
    return pop

