#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:02:32 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt


m = np.loadtxt("stalplat.txt", dtype=float)

fig, ax = plt.subplots()

# We are spplitting the area into 100 pieces, so we will treat this value as a constant since it is the same for all the small areas
A = 1e-2 
# material constant
e = 0.6
# Boltzmann constant
sigma = 5.67e-8

# Construct the complete expression, taking into consideration the plate emits heat from both sides, so we multiply by 2
P = lambda T : 2*A*e*sigma*(T**4 - 300**4)

total = 0.0
for i in range(0, 10):
    for j in range(0, 10):
        total += P(m[i,j])



plt.xticks(range(0,10,1), range(1,11,1))
plt.yticks(range(0,10,1), range(1,11,1))


ax.set_title("Exercise 5")
ax.set_xlabel("Total emmited power = %.2f" %(total), fontsize=8)
ax.imshow(m, cmap='hot')