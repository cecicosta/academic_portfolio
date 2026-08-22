#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:57:30 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Plot the radial density functions for 3s, 3p, 3d and Z = 1 in the
# same plot. Carefully note how the 3s has a larger probability to be close to the nucleus.
# =============================================================================


def P3s(r, Z):
    k = (2/(3*np.sqrt(3))) * (1 - (2/3)*Z*r + 2/27*(Z**2)*(r**2))
    exp = np.exp(-Z*(r/3))
    Zpwr = (Z**(3/2)) 
    return k * Zpwr * r * exp

def P3p(r, Z):
    k = (8/(27*np.sqrt(6))) * (1 - (1/6)*Z*r)
    exp = np.exp(-Z*(r/3))
    Zpwr = (Z**(5/2)) 
    return k * Zpwr * (r**2) * exp

def P3d(r, Z):
    k = (4/(81*np.sqrt(30)))
    exp = np.exp(-Z*(r/3))
    Zpwr = (Z**(7/2)) 
    return k * Zpwr * (r**3) * exp

fig, ax = plt.subplots()
ax.set_title("Exercise 3", fontsize=18)

x = np.linspace(0, 100, 1000)
Z = 1 

ax.plot(x, P3s(x, Z)**2, label="3s")
ax.plot(x, P3p(x, Z)**2, label="3p")
ax.plot(x, P3d(x, Z)**2, label="3d")

ax.grid()
ax.legend()