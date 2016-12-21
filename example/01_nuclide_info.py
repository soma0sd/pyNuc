# -*- coding: utf-8 -*-
import pynuc as pn
import numpy as np
from matplotlib import pyplot as plt

"""get element"""
elem1 = pn.nuclide('092235')
elem2 = pn.nuclide('238U')


"""print info"""
print(elem1)
print(elem2)

"""decay curve plot"""
t = np.logspace(1, 18)
plt.ylim(1E-2, 1.2)
plt.plot(t, elem1.decay(t))
plt.plot(t, elem2.decay(t))
plt.xscale("log", nonposx='clip')
plt.grid(True)
plt.show()
