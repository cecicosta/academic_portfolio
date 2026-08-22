#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 14:00:13 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
tol = float(input(" Give value of tol "))
T0 = (650/4)*np.ones((100,100)) # initialization
T0[0,:] = 100; T0[99,:] = 200 # edge temperatures
T0[:,0] = 100; T0[:,99] = 250
T0[30:51,20:41] = 225 
T1 = np.copy(T0) 
diff = tol + 1 # copy, T1 same edge

# temperature as T0
while diff > tol:
    for i in range(1,99): # loop over inner points
        for j in range(1,99):
            if(not (i >= 30 and i <= 50 and j >= 20 and j <= 40)):
                T1[i,j] = (T0[i+1,j]+T0[i-1,j]+T0[i,j+1]+T0[i,j-1])/4

    diff = np.max(np.abs(T1[1:99,1:99]-T0[1:99,1:99]))
    T0 = np.copy(T1) # T0 copy of T1, not T0=T1

fig, ax = plt.subplots()
pos = ax.imshow(T1,cmap="hot") # plot
cbar = fig.colorbar(pos)
cbar.ax.tick_params(labelsize=14)
ax.tick_params(labelsize=14)