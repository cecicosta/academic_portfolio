#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 14:40:08 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

fig, ax = plt.subplots();

# The following values (A, [kBq]) represents the decay of a raioactive sample, according to the exercise 3,
# in relation to time (x, t[s])
A = [205, 130, 85, 65, 42, 25, 15]
x = [0, 1, 2, 3, 4, 5, 6]

# Following the exercise requests, we first plot the sample values as scattered points
ax.scatter(x, A)

# Following the given function model representing the sample decay, we plot the curve on the specified interval
t = np.linspace(0, 6, 100)
At_lambda = lambda t: 202*np.exp(-0.42*t)
At = At_lambda(t)

# Plot the function with the function legend
ax.plot(t, At, label=r"$A(t)=202e^{-0.42t}$")

# Following the exercise suggestion, to find the sample half-life we subtract 101 from the original function

Ft = lambda t : 202*np.exp(-0.42*t) - 101

# Finding the new equation root, we obtain the time the sample reaches its half-life
Ft_hl = optimize.brentq(Ft, 0, 6)
ax.annotate(rf"$half-life = {{{Ft_hl:.3}}}$", xy = (Ft_hl, 101), xytext=(2.2, 150),arrowprops=dict(width=1))

ax.set_xlabel("t [s]", fontsize=14)
ax.set_ylabel("A [kBq] ", fontsize=14)
ax.legend(loc="upper right", fontsize=10)
ax.set_title("Assignment 1 - Exercise 3")
ax.grid()

