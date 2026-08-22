#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:03:40 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt

# This program reads a text file containing a matrix and create an image from the values read
# Following, to "fix" some artifacts on the image, it replaces pixels with value 0, with a interpolated
# value from its beighbors

m = np.loadtxt("CCD.txt")


# Iterate over the matrix m and compare each value to find which pixels are 0
for i in range(0, m.shape[0]):
    for j in range(0, m.shape[1]):
        if(m[i,j] == 0):
            # We obtain a submatrix 3, 3 based on the current i, j neighbors 
            # From tests we verified the program would fail to get a submatrix if the addresses were out-of-range
            # However, not not being the case for this exercise, we will skip making a more rebust version
            sub_m = m[i-1:i+2, j-1:j+2]
            # Calculate the mean value from the submatrix elements sum
            m[i,j] = sub_m.sum()/8
        


            
fig, ax = plt.subplots()

ax.imshow(m, vmin=3, vmax=7, cmap="gray")


