# -*- coding: utf-8 -*-

def GetElementSymbol():
  data = {}
  with open('elements.csv', 'r') as f:
    for l in f.readlines():
      item = [i.strip() for i in l.split(',')]
      data[int(item[0])] = {'sym': item[1], 'name': item[2]}
  return data
