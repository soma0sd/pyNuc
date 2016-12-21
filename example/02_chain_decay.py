# -*- coding: utf-8 -*-
import pynuc as pn
import numpy as np
from matplotlib import pyplot as plt

"""get chain"""
elem = pn.nuclide('235U')
chain = elem.get_chain()

"""chain element 1D list"""
mixture = chain.decay_mixture() # key list

"""plot chain decay"""
t = np.logspace(-1, 21)
N = chain.decay(t)
plt.title('Decay curve')
plt.ylim(1, 5E30)
for key in N.keys():
  plt.plot(t, N[key]*1E30, label=key)
plt.loglog()
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, ncol=3, borderaxespad=0.)
plt.show()

"""plot chain activity"""
t = np.logspace(-1, 21)
N = chain.activity(t)
plt.title('activity curve')
plt.ylim(1, 1e15)
for key in N.keys():
  plt.plot(t, N[key]*1E30, label=key)
plt.loglog()
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, ncol=3, borderaxespad=0.)
plt.show()
