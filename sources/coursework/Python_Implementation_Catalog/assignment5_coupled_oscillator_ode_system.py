#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 19:41:30 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# The original differential equantions system of second order is transformed into a system of first order
# The equations on represents the right side of the system's equations on the respective order [u0', u1', u2', u3']
f = lambda t, u : [u[1], -2*u[0] + u[2], u[3], u[0] - u[2]]

# Given values for the conditions
U0 = 10
U1 = 0
U2 = 15
U3 = 0

fig, ax = plt.subplots()

s = integrate.solve_ivp(f, [0, 20], [U0, U1, U2, U3], t_eval=np.linspace(0, 20, 1000))

# Plot Y0(u) and Y1(u)
ax.plot(s.t, s.y[0], label=r"$y_0(x)$" )
ax.plot(s.t, s.y[2], label=r"$y_1(x)$")

ax.legend()

ax.set_title("Exercise 2")
ax.set_ylabel(r"Values for y(x)", fontsize=10)
ax.set_xlabel(r"x", fontsize=10)

ax.grid()
