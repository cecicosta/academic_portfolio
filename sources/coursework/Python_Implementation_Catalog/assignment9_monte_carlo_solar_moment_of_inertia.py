#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:13:06 2026

@author: cecilia.costa
"""

import numpy as np

R = 6.96e8 # Sun's radius in metter
N = 10**5 # Number of samples generated

# Density in radius coordinate g/cm^3 -> (10^-3 kg)  / (10^-6 m^3) -> kg/m^3 x 10^3
def rho_x(x):
    return (2139*x + 155)*np.exp(-13.8*x) * 10**3


rho_sum = 0;
I_sum = 0

for _ in range(0, N):
    # Generate a random coordinate withing the enclosing volume
    x = 1 - 2*np.random.rand()
    y = 1 - 2*np.random.rand()
    z = 1 - 2*np.random.rand()
    d = np.sqrt(x**2 + y**2 + z**2)
    # Verify if the point generated is inside the sun (using radius coordinates)
    if(d <= 1):
        rho = rho_x(d)
        rho_sum = rho_sum + rho    
        # Considering z as the rotating axis
        I_sum = I_sum + rho*((R*x)**2 + (R*y)**2 )

m = 8*R**3 * rho_sum / N 
In = 8*R**3 * I_sum / N

print("Sun's mass: %e"  %m)
print("Sun's mementum of inertia: %e"  %In)

m_nsa = 1.989e30
r_nsa = 6.96e8

print("NASA data:" ) 
print("Sun's mass: %e" %m_nsa)
print("Sun's mementum of inertia: %e"  % (0.059 *(m_nsa*r_nsa**2)))

