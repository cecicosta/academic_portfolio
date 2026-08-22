#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:57:30 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Plot orbitals P1s(r) in the same gure for Z = 1,2,3,4
# =============================================================================

def P1s(r, Z):
    k = 2
    exp = np.exp(-Z*r)
    Zpwr = Z**(3/2)
    return k * Zpwr * r * exp

fig, ax = plt.subplots()
ax.set_title("Exercise 2", fontsize=18)

x = np.linspace(0, 10, 1000)
Z = 1 

ax.plot(x, P1s(x, 1), label=r"1s, $Z=1$")
ax.plot(x, P1s(x, 2), label=r"1s, $Z=2$")
ax.plot(x, P1s(x, 3), label=r"1s, $Z=3$")
ax.plot(x, P1s(x, 4), label=r"1s, $Z=4$")

ax.grid()
ax.legend()