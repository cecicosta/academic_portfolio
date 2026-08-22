#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 16:16:10 2026

@author: cecilia.costa
"""

import numpy as np
import scipy.integrate as integrate

Pr = lambda r : 0.084/(1 + np.exp(2*r - 8))

r = np.linspace(0, 8, 1000)

Pcompose = lambda r : 4 * np.pi * Pr(r) * (r**2)
Q = integrate.simpson(Pcompose(r), r)
print("Estimation for nucleous total charge Q=%f" %(Q))
