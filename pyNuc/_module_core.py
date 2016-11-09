# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:41:13 2016
@author: soma0sd
"""
import pyNuc
import inspect
import os

class path:
  def pyNuc():
    return os.path.dirname(inspect.getfile(pyNuc))

  def ensdf():
    return os.path.join(path.pyNuc(), 'ENSDF')


if __name__ == '__main__':
  from pyNuc._module_core import path as p
  print('pyNuc:', p.pyNuc())
  print('ENSDF:', p.ensdf())
