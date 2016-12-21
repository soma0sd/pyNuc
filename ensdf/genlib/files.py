# -*- coding: utf-8 -*-


def get_file_path():
  import os
  import re
  data = []
  root = os.path.dirname(__file__)
  root = os.path.join(root, '..')
  rx = re.compile('ensdf_\d{6}_\d{3}')
  root = [os.path.join(root, i) for i in os.listdir(root) if rx.match(i)]
  for dr in root:
    data += [os.path.join(dr, i) for i in os.listdir(dr)]
  return data

def get_file(A:int=0):
  path = get_file_path()
  if A < 1 or A >= len(path):
    print('file path error')
    return None
  return open(get_file_path()[A-1], 'r')

def get_all_files():
  return [open(i, 'r') for i in get_file_path()]


def get_nist_file():
  from os import path
  from ensdf import genlib
  dr = path.abspath(path.join(path.abspath(genlib.__file__), '..'))
  return open(path.join(dr, 'nist_m_comp.asc'), 'r')
