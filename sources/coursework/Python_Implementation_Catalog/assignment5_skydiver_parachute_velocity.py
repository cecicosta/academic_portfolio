#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 19:41:30 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


# Initial velocity of the sky diver
v0 = 20
# Sky diver's mass
m = 100
# Assuming gravity accelaration as 10 m/s^2
g = 10
# constant given for the parachute breaking force expression
k = 40

# Diferential equation for expressing the sky diver's accelaration after opening the parachute 
f = lambda t, v : [g - (k/m)*v**2]

fig, ax = plt.subplots()

# Resolve the ODE
s = integrate.solve_ivp(f, [0, 10], [v0], t_eval=np.linspace(0, 10, 100))

ax.plot(s.t, s.y[0], label=r"$v(t)$" )

ax.legend()

ax.set_title("Exercise 3")
ax.set_ylabel(r"Velocity v(t) [m/s]", fontsize=10)
ax.set_xlabel(r"Time t [s]", fontsize=10)

# The sky diver terminal force is reach when the acceleration is 0, hence the velocity is constant
ax.annotate(format(r"Terminal Velocity = %.2f" %s.y[0][20]), xy=[s.t[20],s.y[0][20]], xytext=[4, 8], arrowprops=dict(width=1))


ax.grid()
