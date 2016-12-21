# -*- coding: utf-8 -*-
"""
[pynuc] initialization
"""
def _get_path():
  import pynuc as _this
  import os.path as _path
  return _path.abspath(_path.join(_path.abspath(_this.__file__), '..'))

def _get_nuc_data():
  import pickle as _pkl
  import os.path as _path
  dr = _get_path()
  data = _pkl.load(open(_path.join(dr, 'nucinfo.pkl'), 'rb'))
  return data

def _get_nist_data():
  import pickle as _pkl
  import os.path as _path
  dr = _get_path()
  data = _pkl.load(open(_path.join(dr, 'nist.pkl'), 'rb'))
  return data

try:
  _data_nuc
except:
  _data_nuc = _get_nuc_data()

try:
  _data_nist
except:
  _data_nist = _get_nist_data()

from pynuc._c_nuclide import nuclide
from pynuc._c_chain import chain

