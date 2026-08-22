#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 17:50:06 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt


# Size of the string during each instance of the experiment
l_sample = [40, 35.5, 29.5, 23.3, 19, 16, 12, 10]

# Total time afte 10 swings from the pendulum
t_sample = np.array( [13.48, 12.55, 11.70, 10.58, 9.63, 9.22, 8.14, 7.60])

# Estimation for the time taken per swing of the pendulum on the respective experiment instance
t_swing =  t_sample / 10


# Method used to create the interpolation function
f = lambda L : 0.287*L**0.419
ft = lambda T :  (T/0.287)**(1/0.419)
# Define set of values in a rasonable interval to apply the interpolated function,
# and obtain the corresponding image for plotting a smooth curve.
xp = np.linspace(5, 40, 350)  # dense grid for plotting
yp = f(xp)  # function value for spline



fig, ax = plt.subplots()
ax.plot(l_sample, t_swing, 'o')  # plot data points and function
ax.tick_params(labelsize=14)

ax.plot(xp, yp)  # plot data points and function
ax.tick_params(labelsize=14)

ax.legend(["Sample data", r"$T=0.287.L^{0.419}$"])

l_targ = ft(1)
print(l_targ)

ax.annotate(format("(%.3f, 1)" %(l_targ)) , xy = [l_targ, 1], 
            xytext=[l_targ + 3, 0.75], 
            arrowprops=dict(width=1),
            ha='left', va='bottom')


# Create the dashed lines to highlght the target
plt.vlines(l_targ, 0, 1, linestyle="dashed")
plt.hlines(1, 0, l_targ, linestyle="dashed")


#################################################################
# Format the plotted function and data for better vizualization #
#################################################################


plt.xlim(0,None)
plt.ylim(0,None)

ax.grid()

# Add further information for the graphic axis and title
ax.set_title("Exercise 2d")
ax.set_ylabel("Time taken between swings (s)", fontsize=10)
ax.set_xlabel("String size L (cm)", fontsize=10)
