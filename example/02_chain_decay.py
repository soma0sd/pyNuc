# -*- coding: utf-8 -*-
import pynuc as pn

elem = pn.nuclide('238U')
chain = elem.get_chain()
print(chain.decay_mixture())