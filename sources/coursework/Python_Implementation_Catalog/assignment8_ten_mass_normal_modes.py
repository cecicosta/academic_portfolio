#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:31:44 2026

@author: cecilia.costa
"""

# This program is a modified version from the 2 masses x string 
# oscilator simulation from section 11.20, from the lecture notes document.
# This modified version simulates 10 masses instead of 2.

import numpy as np
import matplotlib.pyplot as plt

plt.ion()
# Create the 10 x 10 matrix extracted from the 10 masses system, 
# for which we must find the eigenvalues and eigen vectors
A =  [
      np.hstack([-2, 1, np.zeros(8, dtype=int)]),
      np.hstack([1, -2, 1, np.zeros(7, dtype=int)]),
      np.hstack([0, 1, -2, 1, np.zeros(6, dtype=int)]),
      np.hstack([0, 0, 1, -2, 1, np.zeros(5, dtype=int)]),
      np.hstack([0, 0, 0, 1, -2, 1, np.zeros(4, dtype=int)]),
      np.hstack([np.zeros(4, dtype=int), 1, -2, 1, 0, 0, 0]),
      np.hstack([np.zeros(5, dtype=int), 1, -2, 1, 0, 0]),
      np.hstack([np.zeros(6, dtype=int), 1, -2, 1, 0]),
      np.hstack([np.zeros(7, dtype=int), 1, -2, 1]),
      np.hstack([np.zeros(8, dtype=int), 1, -2]),
      ]

# Find the matrix eigenvalues and eigenvectors
w, v = np.linalg.eig(A)

## Represents the length between each mass
l = np.arange(0,12)

# From the characteristic equation for u(t) = sin(k.t + s).c -> u''(t) = -k^2.sin(k.t + s).c
# When writing the eigenvalue problem form, the eigenvalue lambda, replaces -k^2
# Select 2 different states to be combined
k1 = np.sqrt(-w[0]) 
k2 = np.sqrt(-w[2])
fig, ax = plt.subplots()

i = np.hstack([0, np.random.rand(10), 0]) # make the movement interesting with some initial perturbation
for t in np.arange(0,10*np.pi,0.2):
    # Combine 2 states, applying their respective k and eigenvector.
    # The oscillatory system should now be described by the combination of 2 waves.
    u = np.sin(k1*t)*np.hstack([0,v[:,0],0]) + np.sin(k2*t)*np.hstack([0,v[:,2],0])
    ax.plot(l,u,l,u,'o')
    ax.set_ylim([-1,1])
    ax.tick_params(labelsize=14)
    plt.pause(0.1)
    ax.cla()


plt.ioff()
plt.show()