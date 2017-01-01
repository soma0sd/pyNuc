# -*- coding: utf-8 -*-
from dbgen import __file__ as _root

from os import path as _path
from os import listdir as _listdir
import re as _re


def path_root():
  return _path.abspath(_path.join(_root, ".."))

def path_rawdata():
  return _path.join(path_root(), 'downloads')

def path_ensdf_dir():
  regex = _re.compile("ensdf_[\d]{6}_[\d]{3}")
  root = path_rawdata()
  return [_path.join(root, i) for i in _listdir(root) if regex.match(i)]

def path_ensdf_file():
  data = []
  dirs = path_ensdf_dir()
  for dr in dirs:
    for fr in _listdir(dr):
      data.append(_path.join(dr, fr))
  return data

def path_reference(filename=''):
  return _path.join(_path.join(path_root(), 'refdata'), filename)

def file_ensdf():
  data = []
  path = path_ensdf_file()
  for p in path:
    data.append(open(p, 'r'))
  return data
