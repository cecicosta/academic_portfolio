#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 14:53:53 2026

@author: cecilia.costa
"""

import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt


# The exercise requires plotting the correspondent values for Tensile Fail 
# Limit in 2 different systems, N/m^2 and Brinell HB. Using a given conversion
# table to create a interpolation using splines based on one of the lecture examples.

# The values given by the conversion table
x = [255, 270, 285, 305, 320, 350, 385, 415, 450, 480, 510, 545] # N/m^2
y = [76.0,80.7, 85.5, 90.2, 95.0, 105, 114, 124, 133, 143, 152, 162] # Brinell HB

# Method used to create the interpolation function
f = interp.interp1d(x, y, kind='cubic', fill_value='extrapolate')

# Define set of values in a rasonable interval to apply the interpolated function,
# and obtain the corresponding image for plotting a smooth curve.
xp = np.linspace(250, 600, 350)  # dense grid for plotting
yp = f(xp)  # function value for spline


fig, ax = plt.subplots()
ax.plot(x, y, 'o', xp, yp)  # plot data points and function
ax.tick_params(labelsize=14)

# find the target values we seek from the interpolated function
target_x = 290
target_y = f(290)

#################################################################
# Format the plotted function and data for better vizualization #
#################################################################

# Create the dashed lines to highlght the target
plt.vlines(target_x, 0, target_y, linestyle="dashed")
plt.hlines(target_y, 0, target_x, linestyle="dashed")

# Limit the graphic to the interval we are interested in
plt.xlim(250,None)
plt.ylim(70,None)

# Add a specfic tick mark for the value of the target
plt.yticks(list(plt.yticks()[0]) + [target_y])

# Annotate the graphic to point out the meaning of the value we seek
ax.annotate(r"Brinell HB-value for $290N/m^2$", xy = [290, f(290)], 
            xytext=[290, f(290)+50], 
            arrowprops=dict(width=1),
            ha='left', va='bottom')

# Add further information for the graphic axis and title
ax.set_title("Exercise 1")
ax.set_xlabel(r"Tensile Fail Limit (TFL) in $N/m^2$", fontsize=10)
ax.set_ylabel("Correspondent TFL in Brinell HB", fontsize=10)

