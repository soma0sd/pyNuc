# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:01:02 2016
@author: soma0sd
"""
import numpy as np


class pyNucError(Exception):
    pass


class isotope:
    def __init__(self, *arg: "A, Z", **kw):
        if not len(arg) == 2:
            raise pyNucError("isotope format: isotope(A: int, Z: int)")
        A, Z = arg[0], arg[1]  # find from ENSDF
        self.info = {'A': 1, 'Z': 1, 'dc': 0}
        self.info.update(kw)

    def __repr__(self):
        return "E:{}{:03}".format(self.info['Z'], self.info['A'])


class bateman_sol:
    def __init__(self, *chain):
        self.dc = dc = [i.info['dc'] for i in chain]
        self.Cn = []
        num = 1
        for d in dc[:-1]:
            num *= d
        for d1 in dc:
            den = 1
            for d2 in dc:
                if not d1-d2 == 0:
                    den *= (d2-d1)
            self.Cn.append(num/den)

    def __repr__(self):
        prstr = "{:.3}EXP(-{}t)".format(self.Cn[0], self.dc[0])
        for i in range(1, len(self.Cn)):
            prstr += " + {:.3}EXP(-{}t)".format(self.Cn[i], self.dc[i])
        return prstr

    def population(self, time, ratio=1):
        result = 0
        for i, C in enumerate(self.Cn):
            result += C*ratio*np.exp(-self.dc[i]*time)
        return result

if __name__ == '__main__':
    import pyNuc as pn
    e1 = pn.isotope(A=1, dc=1)
    e2 = pn.isotope(A=2, dc=0.5)
    e3 = pn.isotope(A=3, dc=0.25)
    b1 = bateman_sol(e1)
    print(b1)
    print(b1.population(0))
