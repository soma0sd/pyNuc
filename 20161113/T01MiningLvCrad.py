# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 01:43:42 2016
@author: soma0sd

create 'IsoLevels.pkl' File.
That file has 'Adopted levels' card without comments
"""
def run():
  import ENSDF as sub
  import pickle as pkl

  FilePath = sub.data_path()
  Levels = []
  """
  ADOPTED LEVELS Card Mining
    + comments remove

  data header [0]
    [0:5] NUCID
  """
  for path in FilePath:
    with open(path, 'r') as f:
      card = []
      for line in f.readlines():
        if line.strip() is '':
          if 'ADOPTED LEVELS' in card[0]:
            Levels.append(card)
            card = []
          else:
            card = []
        else:
          if not 'c' in line[6:9] and not 'C' in line[6:9]:
            card.append(line.strip('\n'))
  del card, line, path, FilePath
  """
  Pickling Data
    file name: 'IsoLevels.pkl'
  """
  with open('LevelCards.pkl', 'wb') as f:
    pkl.dump(Levels, f)
