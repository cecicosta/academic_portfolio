#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 19:41:30 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


Y0 = 0
Y1 = 0

f = lambda x, y : [y[1], np.sin(x) - y[0] ]

fig, ax = plt.subplots(2, 1)

s = integrate.solve_ivp(f, [0, 10], [Y0, Y1], t_eval=np.linspace(0, 10, 1000))

ax[0].plot(s.t, s.y[0], label="y" )
ax[0].plot(s.t, s.y[1], label="dy/dx")

ax[0].legend()

ax[0].set_title("Exercise 1b")
ax[0].set_ylabel(r"Values for y(x)", fontsize=10)
ax[0].set_xlabel(r"x", fontsize=10)

ax[0].grid()


ax[1].plot(s.y[0], s.y[1])


ax[1].set_ylabel(r"Values for y'(x)", fontsize=10)
ax[1].set_xlabel(r"y(x)", fontsize=10)

ax[1].grid()
