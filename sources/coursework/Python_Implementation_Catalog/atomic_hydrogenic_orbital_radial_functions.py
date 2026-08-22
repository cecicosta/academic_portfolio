#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:57:30 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Set Z = 1 and plot the hydrogenic orbitals P1s(r),...,P3d(r) in the same
# gure. Test dierent intervals for r until you are happy with the result.
# Use gtext to interactively put text in the plot
# =============================================================================

def P1s(r, Z):
    k = 2
    exp = np.exp(-Z*r)
    Zpwr = Z**(3/2)
    return k * Zpwr * r * exp

def P2s(r, Z):
    k = (1/np.sqrt(2)) * (1 - (1/2)*Z*r)
    exp = np.exp(-Z*(r/2))
    Zpwr = (Z**(3/2)) 
    return k * Zpwr * r * exp

def P2p(r, Z):
    k = (1/(2*np.sqrt(6)))
    exp = np.exp(-Z*(r/2))
    Zpwr = (Z**(5/2)) 
    return k * Zpwr * (r**2) * exp

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
ax.set_title("Exercise 1", fontsize=18)

x = np.linspace(0, 50, 1000)
Z = 1 

ax.plot(x, P1s(x, Z), label="1s")
ax.plot(x, P2s(x, Z), label="2s")
ax.plot(x, P2p(x, Z), label="2p")
ax.plot(x, P3s(x, Z), label="3s")
ax.plot(x, P3p(x, Z), label="3p")
ax.plot(x, P3d(x, Z), label="3d")

ax.grid()
ax.legend()