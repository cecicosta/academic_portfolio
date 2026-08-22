#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 16:43:48 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt


# This program reads a text file containing datapoints from CO2 concentration on the atmosphere

# We create the x axis values based on the years in which the sample data was collected, 
# breaking the interval into the number of datapoints we possess
x = np.linspace(2000, 2025, 1357, dtype=float)

# Reads the file
m = np.loadtxt("co2.txt")
max_v = m.max()
min_v = m.min()

# Select the sub interval corresponding the the weeks of 2000
sub_2000 = m[:53]
mean_2000 = sub_2000.mean()

# Select the sub interval corresponding to the weeks of 2025
sub_2025 = m[1305:1357]
mean_2025 = sub_2025.mean()

fig, ax = plt.subplots()

ax.set_title("Exercise 3d")
ax.set_xlabel("2000-2025 (weekly measure)", fontsize=8)
ax.set_ylabel("Atmospheric CO2 concentration (ppm) ", fontsize=8)

ax.annotate("2000 mean value = %.2f"  %(mean_2000), xy = (2000, mean_2000), xytext=(2000, 405),arrowprops=dict(width=1), fontsize=8)
ax.annotate("2025 mean value = %.2f"  %(mean_2025), xy = (2025, mean_2025), xytext=(2010, 427),arrowprops=dict(width=1), fontsize=8)


ax.grid()
ax.plot(x, m, "+", label="Min = %.2f \nMax = %.2f" %(min_v, max_v))
ax.legend(loc="upper left", fontsize=10)


