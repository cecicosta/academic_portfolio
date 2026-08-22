
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 22:45:17 2026

@author: cecilia.costa
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# Particle velocity
v = 1.53e7
# Charge of the gold nucleous
Q = 79
# Charge of the alpha particle
q = 2
# Constant from electric force expression
K = 3.477e13

# Initial conditions stablished by the exercise, with dependency on b (impact factor)
cond = lambda b : [-1e6, v, b, 0]

def ScatteringAngle(b) :
    u = (v**4 * b**2) / (K*Q*q)**2
    sin_h_angle = 1 / (np.sqrt( 1 + u )) # Expression for the sin(x/2)
    return np.arcsin(sin_h_angle) * 2 # arcsin will give the value of x/2

# Create the image with a fixed size to accomodate the 3 plots
fig, ax = plt.subplots(5, 1, figsize=(8, 12), constrained_layout=True)
ax[0].set_title("Exercise 2", fontsize=18)

# ODE system with variable substitution
ODE = lambda t, u: [
    u[1],
    K*Q*q * u[0] / (u[0]**2 + u[2]**2)**1.5,
    u[3],
    K*Q*q * u[2] / (u[0]**2 + u[2]**2)**1.5
]


i = 0 # Use to iterate over Axis instances

# Iterate over the different given values for the impact factor b
for b in [25, 0, 10, 50, 100]:

    # Resolve ODE system for given conditions
    sol = integrate.solve_ivp(
        ODE,
        [0,0.1], cond(b), t_eval=np.linspace(0, 0.1, 1000), rtol=1e-9, atol=1e-12)
    
    # Set Axis info and format
    ax[i].set_xlabel(r"$x(t)$",fontsize=14)
    ax[i].set_ylabel(r"$y(t)$",fontsize=14)
    ax[i].tick_params(labelsize=14)    

    angle = ScatteringAngle(b)

    # Plot values for the trajectory (x(t),y(t))
    ax[i].plot(sol.y[0],sol.y[2], label=r"b={}, $\theta={:.1f}$ degrees".format(b, np.degrees(angle)))


    # Further plot setup
    ax[i].legend(loc="upper left", fontsize=12)
    ax[i].set_xlim(-1e6, 0.4e6)

    # Increment i for the next plot
    i = i + 1
    
    
