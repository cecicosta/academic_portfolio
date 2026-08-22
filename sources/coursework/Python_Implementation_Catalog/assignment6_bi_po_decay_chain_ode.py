
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 22:45:17 2026

@author: cecilia.costa
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# Decay constants for 210 Bi and 210 Po, respectivelly
lmbda_0 = np.log(2)/5.01
lmbda_1 = np.log(2)/138.38

# Y_0(0) and Y_1(0) respectively
cond = [1, 0]

# Interval for which to resolve the ODE
t_lim = [0, 100]
t_eval = np.linspace(0, 100, 1000) 

# ODE representing the compartiment model for the radioactive decay chain of 210 Bi
def ODE(t, y) :
    return [-lmbda_0*y[0], lmbda_0*y[0] - lmbda_1*y[1]]


# Prepare the image for the plot
fig, ax = plt.subplots(figsize=(8, 3), constrained_layout=True)
ax.set_title("Exercise 3", fontsize=18)

# Resolve ODE system for the given conditions
sol = integrate.solve_ivp(
    ODE,
    t_lim, 
    cond, 
    t_eval=t_eval)

# Set Axis info and format
ax.set_ylabel(r"$y(t)\ [quantity]$",fontsize=14)
ax.set_xlabel(r"$t [time]$",fontsize=14)

ax.tick_params(labelsize=14)    


# Plot values for the quantities of both elements over time
ax.plot(sol.t,sol.y[0], label=r"$^{210}$Bi, decay")
ax.plot(sol.t,sol.y[1], label=r"$^{210}$Po, decay")

# Find the index of the max value of 210 Po
i = np.where(sol.y[1] == sol.y[1].max())[0]

# The index i correspont to the max value of 210 Po and its corresponding value of time in the t axis
y = sol.y[1][i][0] 
t = sol.t[i][0]

print("Maximum quantity of PO is {} mols, at time {}".format(y, t))
# Create the dashed lines to highlght the target
ax.vlines(t, 0, y, linestyle = "dashed" )
ax.hlines(y, 0, t, linestyle = "dashed" )

ax.set_xticks([0,50,75,100] + [t])
ax.set_yticks([0,0.5,1] + [y])

# Further plot setup
ax.legend(loc="upper right", fontsize=11)


