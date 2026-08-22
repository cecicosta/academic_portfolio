#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:51:16 2026

@author: cecilia.costa
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
c = 0.25
g = 9.81


# As the initial velocity on both components x,y are the same, we can assume the 
# throwing angle to be 45 degrees, and the initial velocity 20 m/s
v = 150
cond = lambda alpha : [0,v*np.cos(np.radians(alpha)),0,v*np.sin(np.radians(alpha))]

fig, ax = plt.subplots()

ax.set_title("Exercise 5 - Ball throw with friction")

ax.set_xlabel("x",fontsize=14)
ax.set_ylabel("y",fontsize=14)
ax.tick_params(labelsize=14)


traj = lambda t,z: [z[1],-c*np.sqrt(z[1]**2 + z[3]**2)*z[1], z[3],-c*np.sqrt(z[1]**2 + z[3]**2)*z[3] -g]

# Modifying the condition from z2 = 1 (z2 = y as the variables were changed) to z2 = 0
position = lambda t,z: z[2] 

# The direction still points downwards, so we are still keeping the condition of the descending tragectory
position.direction = -1 # z[2] decreasing with t for

# the event to be true, the ball
# should be on its way down
position.terminal = True # integration terminates at event

x_max = 0
angle = 45
t_end = 0
for i in range(1, 89):    
    sol0 = integrate.solve_ivp(traj,[0,10],cond(i), events=position)
    x_end = float(sol0.y_events[0][0][0])
    if(x_end > x_max):
        x_max = x_end
        angle = i
        t_end = float(sol0.t_events[0][0])
        
        

print("Further distance x for which y(t) = 0 is", x_max)
print("Maximum distance reach at angle", angle)



# Solves in the the interval [0,t_end], outputs solution on
# dense grid
sol = integrate.solve_ivp(traj,[0,t_end],cond(angle),t_eval=np.linspace(0,t_end,100))

function_label = format(r"$\theta=%i,\ x=%.2f, v=%.2f$" %(angle, x_max, v))
# plot y vs x, i.e. we get a parabola
ax.plot(sol.y[0],sol.y[2], label=function_label)
ax.legend(loc="upper left")



