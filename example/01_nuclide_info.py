# -*- coding: utf-8 -*-
import pynuc as pn
import numpy as np
from matplotlib import pyplot as plt

"""get element"""
elem1 = pn.nuclide('092235') # type 1
elem2 = pn.nuclide('238U')   # type 2


"""print infomation"""
print(elem1)
print(elem2)

"""decay curve plot"""
t = np.logspace(1, 18)
plt.title('decay curve')
plt.ylim(1E-2, 1.2)
p1 = plt.plot(t, elem1.decay(t), label=elem1._asc_code())
p2 = plt.plot(t, elem2.decay(t), label=elem2._asc_code())
plt.xscale("log", nonposx='clip')
plt.grid(True)
plt.legend()
plt.show()

"""activity curve plot"""
plt.title('activity curve')
plt.plot(t, elem1.activity(t), label=elem1._asc_code())
plt.plot(t, elem2.activity(t), label=elem2._asc_code())
plt.xscale("log", nonposx='clip')
plt.grid(True)
plt.legend()
plt.show()
