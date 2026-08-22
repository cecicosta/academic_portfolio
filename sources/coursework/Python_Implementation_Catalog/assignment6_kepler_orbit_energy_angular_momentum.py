#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 22:45:17 2026

@author: cecilia.costa
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# Simplification provided by the exercise for the travitational constant times sun's mass
GM = 1
# Represents the planets mass
m = 1

# Expression for potential gravitational energy
def E_p(x, y):
    return -GM*m * ( 1 / np.sqrt(x**2 + y**2) )

# Expression for kinetic energy
def E_k(dx, dy):
    return 0.5 * m * (dx**2 + dy**2)

# Expression for angular momentum on the Z axis
def L_z(x, y, dx, dy):
    return x*dy - y*dx

# Create the image with a fixed size to accomodate the 3 plots
fig, ax = plt.subplots(3, 1, figsize=(8, 12), constrained_layout=True)
ax[0].set_title("Exercise 1.b")

# ODE system with variable substitution from Newton's expression for x''(t) and y''(t)  
ODE = lambda t, u: [
    u[1],
    -GM * u[0] / (u[0]**2 + u[2]**2)**1.5,
    u[3],
    -GM * u[2] / (u[0]**2 + u[2]**2)**1.5
]


i = 0 # Use to iterate over Axis instances

# Iterate over the different values of e for which to calculate the elipse
for e in [0, 0.5, 0.9]:
    cond = [1-e, 0, 0, np.pow((1+e) / (1-e), 1/2)] # Exercise's provided conditions

    # Resolve ODE system for given conditions
    sol = integrate.solve_ivp(
        ODE,
        [0,2*np.pi], cond, t_eval=np.linspace(0, 2*np.pi, 1000),         
        rtol=1e-5, # Sets the relative error tolerance so to avoid previously observed inconsistences on the results. Value found by trial.
        atol=1e-6) # Sets the absolute error tolerance so to avoid previously observed inconsistences on the results. Value found by trial.

    
    # Set Axis info and format
    ax[i].set_xlabel(r"x(t) [$\pi$]",fontsize=14)
    ax[i].set_ylabel(r"y(t) [$\pi$]",fontsize=14)
    ax[i].tick_params(labelsize=14)    
    ax[i].set_aspect("equal", adjustable="box")

    # Plot values for x(t) and y(t)
    E_t =  E_k(sol.y[1],sol.y[3]) + E_p(sol.y[0],sol.y[2])
    ax[i].plot(sol.t, E_t, label=r"$E_k + E_p$")
    
    ax[i].plot(sol.t, E_k(sol.y[1],sol.y[3]), "--", label=r"$E_k$")
    ax[i].plot(sol.t, E_p(sol.y[0],sol.y[2]), "--", label=r"$E_p$")
    ax[i].plot(sol.t, L_z(sol.y[0], sol.y[2], sol.y[1], sol.y[3]), label=r"$L_z$")

    # Further Axis setup
    ax[i].legend(loc="upper left", fontsize=12)
    ax[i].set_xlim(0, 2*np.pi)
    ax[i].set_ylim(-2, 2)

    # Increment i for the next plot
    i = i + 1