# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:12:14 2016
@author: soma0sd

Dev 1.0: based input A, Z
"""
import os
from pyNuc._module_core import path

class Isotope:
  def __init__(self, A: int, Z: int):
    dirs = os.listdir(path.ensdf())
    if 0 < A < 100:
      ensdf_path = os.path.join(path.ensdf(), dirs[0])
    if 99 < A < 200:
      ensdf_path = os.path.join(path.ensdf(), dirs[1])
    if 199 < A < 295:
      ensdf_path = os.path.join(path.ensdf(), dirs[2])
    else:
      raise "Mass Number: out of range (ENSDF)"
    del dirs

if __name__ == '__main__':
  import pyNuc._module_Isotopes as this
  _ = this.Isotope(256, 92)

