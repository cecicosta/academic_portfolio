
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

# Number of particles to simulate numerically
N = 10**3

# Initial conditions stablished by the exercise, with dependency on b (impact factor)
cond = lambda b : [-1e6, v, b, 0]

# Provide the scattering angle for a given impact factor using the analtical formula
def ScatteringAngle(b) :
    u = (v**4 * b**2) / ((K*Q*q)**2)
    sin_h_angle = 1 / (np.sqrt( 1 + u )) # Expression for the sin(x/2)
    return np.arcsin(sin_h_angle) * 2 # arcsin will give the value of x/2

# Provides the impact factor from a scattering angle using the analytical formula
def ImpactFactor(angle) :
    u = (K*Q*q) / v**2
    return u * 1/np.tan(angle/2)

# Provides the differential crosssection used in Rutherford formula
def DifferentialCrossSection(angle):
    u = ((K*Q*q) / (2*v**2))**2 
    return u * 1/(np.sin(angle/2)**4)

# Obtain the maximum impact factor, given by the angle of 50 degrees 
b_max = ImpactFactor(np.radians(50))
print("Impact factor b, for scattering angle 50 degrees: %.2f"  %b_max) 

# Calculate the particle's density for the emission cross section area
I = N / (np.pi*b_max**2)

# Give the number of particles scattered at a given angle interval, according to Rutherford's formula
def NDetectedParticles(angle, deltaAngle):
    return I*DifferentialCrossSection(angle) * 2 * np.pi * np.sin(angle) * deltaAngle

# Obtain the analytical solution for the number of scattered particles per angle interval between 50-180
angle_intervals = np.arange(50.0,180.0,10.0)
particles_per_angle = np.zeros(len(angle_intervals))
for i in range(0, len(angle_intervals)):
    particles_per_angle[i] = NDetectedParticles(np.radians(angle_intervals[i]), np.radians(10))


# ODE system with variable substitution
def ODE (t, u): 
    return [
        u[1],
        K*Q*q * u[0] / (u[0]**2 + u[2]**2)**1.5,
        u[3],
        K*Q*q * u[2] / (u[0]**2 + u[2]**2)**1.5
    ]




scattering_angles = []
i = 0
# Iterate over the different given values for the impact factor b
while i < N:

    by = b_max*np.random.rand() - b_max
    bz = b_max*np.random.rand() - b_max

    b = np.sqrt(by**2 + bz**2)

    
    if(b <= b_max):
        # Resolve ODE system for given conditions
        sol = integrate.solve_ivp(ODE,
                                  [0,0.1], cond(b), 
                                  t_eval=np.linspace(0, 0.1, 1000), rtol=1e-9, atol=1e-12)

        # Here we calculate the time until the impact. The goal is to find from which index
        # of the vector solution we should use the values to start calculating the scattetering 
        # angle numerically
        s = 1e6 # Distance the particle travelled 
        # Obtain the time of the impact and convert to an index from 0-1000, based on the known time interval 
        ti = int((s/v) * 1000/0.1) 
        # Calculate the tangent of the tragectory after the collision
        m = (sol.y[2][-1] - sol.y[2][ti+1]) / (sol.y[0][-1] - sol.y[0][ti+1])
        
        
        angle_rad = np.arctan(m)
        if (angle_rad <= 0):
            angle_rad = np.pi + angle_rad

        scattering_angles.append(np.degrees(angle_rad))
        i = i + 1
            

        
# Create the image with a fixed size to accomodate the 3 plots
fig, ax = plt.subplots()
ax.set_title("Exercise 3", fontsize=18)


# Set Axis info and format
ax.set_xlabel(r"$\theta$ [angle in degrees]",fontsize=10)
ax.set_ylabel(r"$N(\theta)$ [Number of particles]",fontsize=10)
ax.tick_params(labelsize=14)    

angle = ScatteringAngle(b)

# Plot values for the analytical and numerical solution for the number of scattered particles at the given angle intervals
ax.hist(scattering_angles, 13, range=(50, 180), label="Numerical simulation")
ax.plot(angle_intervals, particles_per_angle, label="Analytical solution")

ax.legend()

         
    
