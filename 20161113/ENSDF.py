# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 23:19:51 2016
@author: soma0sd

project basic functions
  def get_
  def sym2int(sym)
    2 space symbol string trans to integer type atomic number
"""


def data_path():
  import ENSDF
  from os import path
  import os
  data = []
  root = path.dirname(ENSDF.__file__)
  root = path.join(root,"..")
  root = path.join(path.abspath(root), 'ensdf')
  list_dr = os.listdir(root)
  for d1 in list_dr:
    m = path.join(root, d1)
    for d2 in os.listdir(m):
      data.append(path.join(m, d2))
  return data

def sym2int(sym: str):
  data = {'NN': 0, 'H ': 1, 'HE': 2, 'LI': 3, 'BE': 4, 'B ': 5, 'C ': 6, 'N ': 7, 'O ': 8, 'F ': 9, 'NE': 10, 'NA': 11, 'MG': 12, 'AL': 13, 'SI': 14, 'P ': 15, 'S ': 16, 'CL': 17, 'AR': 18, 'K ': 19, 'CA': 20, 'SC': 21, 'TI': 22, 'V ': 23, 'CR': 24, 'MN': 25, 'FE': 26, 'CO': 27, 'NI': 28, 'CU': 29, 'ZN': 30, 'GA': 31, 'GE': 32, 'AS': 33, 'SE': 34, 'BR': 35, 'KR': 36, 'RB': 37, 'SR': 38, 'Y ': 39, 'ZR': 40, 'NB': 41, 'MO': 42, 'TC': 43, 'RU': 44, 'RH': 45, 'PD': 46, 'AG': 47, 'CD': 48, 'IN': 49, 'SN': 50, 'SB': 51, 'TE': 52, 'I ': 53, 'XE': 54, 'CS': 55, 'BA': 56, 'LA': 57, 'CE': 58, 'PR': 59, 'ND': 60, 'PM': 61, 'SM': 62, 'EU': 63, 'GD': 64, 'TB': 65, 'Dy': 66, 'DY': 66, 'HO': 67, 'ER': 68, 'TM': 69, 'YB': 70, 'LU': 71, 'HF': 72, 'TA': 73, 'W ': 74, 'RE': 75, 'OS': 76, 'IR': 77, 'PT': 78, 'AU': 79, 'HG': 80, 'TL': 81, 'PB': 82, 'BI': 83, 'PO': 84, 'AT': 85, 'RN': 86, 'FR': 87, 'RA': 88, 'AC': 89, 'TH': 90, 'PA': 91, 'U ': 92, 'NP': 93, 'PU': 94, 'AM': 95, 'CM': 96, 'BK': 97, 'CF': 98, 'ES': 99, 'FM': 100, 'MD': 101, 'NO': 102, 'LR': 103, 'RF': 104, 'DB': 105, 'SG': 106, 'BH': 107, 'HS': 108, 'MT': 109, '10': 110, 'DS': 110, 'RG': 111, 'CN': 112, '12': 112, '13': 113, '14': 114, 'FL': 114, '15': 115, '16': 116, '17': 117, '18': 118}
  return data[sym]

if __name__ == '__main__':
  data = data_path()
  li = []
  for dr in data:
    li.append(int(dr[-3:]))
  for i in range(295):
    if not i in li:
      print(i)
