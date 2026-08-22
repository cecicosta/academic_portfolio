#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 23:09:05 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# This program plots a function for the buoyant force

# Wooden ball radius in m
r = 1

# Wooden ball volume
v = np.pi * r**3 * 4/3

# Submerged area of the sphere
A = lambda x : 2 * np.pi * r * x

# Woden ball density in kg/m^3
Pp = 700

# Water density in kg/m^3
Pv = 1000

# Rounded gravity acceleration in m/s^2
g = 10

w = 2*np.pi*r*g*Pv

# The buoyance force is given by F = g.Pv.x.A, with x being the height of the water collum the ball is
# submerged within.
V = lambda x : np.pi * (x**2 - (x**3)/3)
Fsub = lambda x : g*Pv*V(x)

fig, ax = plt.subplots()

# Define a reasonable interval for plotting the forces affecting the wooden ball
Xs = np.linspace(0, 2)


Yb = Fsub(Xs)

# Draw the function for the buoyance force intensity F(x), with x as measure of how much the ball is submerged
ax.plot(Xs, Yb)

# For the woden ball to reach balance, the bouyance force must balance with the weight force of the ball
Fw = lambda : g * v * Pp

# Draw the functions for the weight force
ax.plot([0, 2], [Fw(), Fw()])

# Equation subtracting the buoyance and weight forces
Eq = lambda x : Fw() - Fsub(x)

# Obtain the root for the equation subtracting the buoyance and weight forces to find where they balance each other
x = opt.brentq(Eq, 0, Xs[-1])

#print(x)

# Trace the point in which the buoyance and weight forces balance each other
plt.vlines(x, 0, Fw(), linestyle="dashed")
plt.hlines(Fw(), 0, x, linestyle="dashed")

plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

# Show only tick marks of interest to avoid poluting the plot
plt.xticks([Xs[0], round(x, 2), 1])
plt.yticks([Fsub(Xs[0]), Fsub(x), Fsub(Xs[-1])])

# Set the max and min limits we want the plot to encompass as the domain and image from the interval we chose
plt.xlim(Xs[0], Xs[-1])
plt.ylim(Fsub(Xs[0]), Fsub(Xs[-1]))

ax.set_title("Exercise 1")
ax.set_ylabel(r"Force in $N$", fontsize=10)
ax.set_xlabel(r"Woden ball submerssion in $m$", fontsize=10)

