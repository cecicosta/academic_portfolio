#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 19:41:30 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from matplotlib.gridspec import GridSpec

#
l = 1
# 
g = 9.81

# Lambda expressing the ODE system of first order obtained from θ′′(t) =−Lsin(θ(t))
# For the angle of a pendulum swinging
f = lambda t, u : [u[1], (-g/l) * np.sin(u[0]) ]

# Analytically obtained expression for the ODE above
u = lambda t, theta: theta * np.cos(np.sqrt(9.81)*t)


# The following sets up the image layout with 2 plots side by size and one bellow occupying the whole lenght
fig = plt.figure(figsize=(8, 6))
gs = GridSpec(2, 2, height_ratios=[1, 1.2])

ax = fig.add_subplot(gs[0, 0])   # top-left
az = fig.add_subplot(gs[0, 1])   # top-right
aw = fig.add_subplot(gs[1, :])   # bottom, spans both columns


# Resolve the ODE system for θ(0) = 0.1 and θ'(0) = 0, withing the interval 0 <= t <= 10
s = integrate.solve_ivp(f, [0, 10], [0.1, 0], t_eval=np.linspace(0, 10, 100))

# Plot the solved ODE system for θ(t)
ax.plot(s.t, s.y[0], label=r"$\theta(t)$" )

# Plot the analytically obtained expression for θ(t)
ax.plot(s.t, u(s.t, 0.1), "--", label=r"$\theta(t)=0.1\ \cos{\sqrt{9.81}t}$")

# Set information for the plot and format
ax.set_title(r"Numerical and analytical comparison for $\theta(0)=0.1$", fontsize=8)
ax.legend(fontsize=8, loc="lower left")
ax.grid()


# Resolve the ODE system for θ(0) = 1 and θ'(0) = 0, withing the interval 0 <= t <= 10
su = integrate.solve_ivp(f, [0, 10], [1, 0], t_eval=np.linspace(0, 10, 100))

# Plot the solved ODE system for θ(t)
az.plot(su.t, su.y[0], label=r"$\theta(t)$" )

# Plot the analytically obtained expression for θ(t)
az.plot(su.t, u(su.t, 1), label=r"$\theta(t)=\cos{\sqrt{9.81}t}$")

# Set information for the plot and format
az.set_title(r"Numerical and analytical comparison for $\theta(0)=1$", fontsize=8)
az.legend(fontsize=8, loc="lower left")
az.grid()

# Plot the comparison between f(x) = sin x and g(x) = x
x = np.linspace(0, 1, 100)
aw.set_title(r"Analysis of curves convergency/divergency withing interval $t=[0, 1]$", fontsize=8)
aw.plot(x, np.sin(x), label=r"$f(x)=sin\ x$")
aw.plot(x, x, "--", label=r"$g(x)=x$")
aw.legend(fontsize=8, loc="upper left")

aw.grid()