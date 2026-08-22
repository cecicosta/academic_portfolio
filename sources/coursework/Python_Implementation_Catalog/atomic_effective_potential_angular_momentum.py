#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:29:34 2026

@author: cecilia.costa
"""


import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Set Z = 1 and plot the effective potential V(r) =−Z/r+ ℓ(ℓ+1)/2r2 
# for s, p, d, and f electrons (see gure 4). Plot all the potentials in
# =============================================================================

Z = 1
def V(r, l):
    return -Z/r + (l*(l+1))/(2*(r**2))

fig, ax = plt.subplots()
ax.set_title("Exercise 8", fontsize=18)

x = np.linspace(0.1, 40, 1000)

ax.plot(x, V(x, 0), label=r"s")
ax.plot(x, V(x, 1), label=r"p")
ax.plot(x, V(x, 2), label=r"d")
ax.plot(x, V(x, 3), label=r"f")

E = np.full_like(x, -0.4)
ax.plot(x, E, "--", label="E", color="cornflowerblue")

E = np.full_like(x, -0.17)
ax.plot(x, E, "--", label="E", color="orange")

E = np.full_like(x, -0.06)
ax.plot(x, E, "--", label="E", color="green")

E = np.full_like(x, -0.03)
ax.plot(x, E, "--", label="E", color="red")



ax.set_ylim(-0.5, 0.5)

ax.grid()
ax.legend(loc="upper right")