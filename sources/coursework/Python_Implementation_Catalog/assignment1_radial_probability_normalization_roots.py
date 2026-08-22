#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 16:21:48 2026

@author: cecilia.costa
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from scipy.integrate import quad


fig, ax = plt.subplots();

x = np.linspace(0, 80, 100)

# First we define a partial version of P(r), with A*P_partial(r) = P(r).
Pr_partial = lambda r: r**2*np.exp(-r/4) * ( 1 - 1/4*r + 1/80*r**2 )

# When resolving the integral of |P(r)|^2, we can separate the constant A, moving it outside the integral as A^2.
# The integral now can be solved with the partial version of P(r) 
Pr_partial_n = lambda r : np.absolute(Pr_partial(r))**2
Pr_partial_i, Pr_partial_err = quad( Pr_partial_n, 0, 80);

# From the definition of P_partial(r), we can now calculate A. 
A = 1/np.sqrt(Pr_partial_i)

# Defines P and P_partial as a lambdas 
Pr = lambda r : A*Pr_partial(r)
Pr_i = lambda r : np.absolute(Pr(r))**2

# Calculate the integral of P_partial on the stablished interval
Pr_sum, Pr_err = quad(Pr_i, 0, 80)

# Calculate P roots, using reasonable interval we know, based on a partial plot. 
Pr_r1 = optimize.brentq(Pr, 2, 10)
Pr_r2 = optimize.brentq(Pr, 10, 20)

# Anotate the ploted curve with the respective found roots
ax.annotate(rf"$P(r) = 0, x={{{Pr_r1:.3}}}$", xy = (Pr_r1, Pr(Pr_r1)), xytext=(10, 1),arrowprops=dict(width=1))
ax.annotate(rf"$P(r)= 0, x = {{{Pr_r2:.3}}}$", xy = (Pr_r2, Pr(Pr_r2)), xytext=(20, -1),arrowprops=dict(width=1))

# Effective plot the curve, with its respetive legend and further format settings for the other elements composing the graphic
ax.set_title("Exercise 4")
ax.grid()
ax.plot(x, Pr(x), label = rf"$P(r)={A:.3}r^{{2}}e^{{-r/4}}(1-\frac{{1}}{{4}}r+\frac{{1}}{{80}}r^{{2}})$")
ax.axis([0, 80, -5, 5])
ax.set_xlabel("r", fontsize=14)
ax.set_ylabel("P(r) ", fontsize=14)
ax.legend(loc="upper right", fontsize=10)



