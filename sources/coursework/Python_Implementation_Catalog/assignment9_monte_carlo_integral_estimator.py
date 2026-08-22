#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:13:06 2026

@author: cecilia.costa
"""

import numpy as np

# Function to be integrated
def F(x):
    return x * np.exp(-x)

# Different values of N, use on each round to obtain the approximation by Monte-Carlo
n = [10**2, 10**3, 10**7]

# Interval to be integrated
x_min = 0
x_max = 10

# Vector use to save the average of the function on each round of MT
F_avg = np.zeros(len(n))

# The most external loop will iterate over the different values of N
for j in range(0, len(n)):
    F_sum = 0;
    # For each value of N, we run MC to obtain an estimation for the integral
    for i in range(0, n[j]):
        # Generate a value of x within the integration interval
        x = (x_max - x_min)*np.random.rand()
        # Calculate f(x) and accumulate
        F_sum = F_sum + F(x)    
    # Once the respective round of MT is finished, we calculate the final value of the integral estimative
    F_avg[j] = ((x_max - x_min) / n[j]) * F_sum 
    print("Integral value for n = %d, is %f" %(n[j], F_avg[j]))
    
print("Analytical solution: 0.99950...");

