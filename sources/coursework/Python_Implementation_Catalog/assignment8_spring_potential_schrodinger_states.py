# -*- coding: utf-8 -*-


"""
This program is a modified version of quantumwell.py.
On this version an oscilatory spring system is modelled 
as an eigenvalue problem applied to the Shrodinger equation.
"""

import numpy as np
import matplotlib.pyplot as plt

n = 500                  # number of grid points
x_min, x_max = -10, 10   # solution interval

# Potential and potential matrix
x = np.linspace(x_min,x_max,n+1)
u = 0.5*x**2

U = np.diag(u[1:n])

# Dicretized differential operator
dx = (x_max - x_min)/n;
L = (2*np.eye(n-1) - np.diag(np.ones(n-2),1) - np.diag(np.ones(n-2),-1))/(2*dx**2)

# Hamilton matrix, H is Hermitian
H = L + U

# Diagonalize and determine E and psi for inner points
w, v = np.linalg.eigh(H)

# Extract and print bound states E < 0
i = 0            # counter
while True:
    if i == 10:
        break
    print("State",i,"E = ",w[i])
    i = i + 1
nbound = i 

# Plot potential and energies
fig, ax = plt.subplots()
ax.plot(x,u)
for i in range(nbound):
    ax.plot([x_min,x_max],[w[i],w[i]],"r")
ax.set_xlabel("x (a0)",fontsize=14)
ax.set_ylabel("E (Eh)",fontsize=14)
ax.set_title("Potential and energies",fontsize=14)
ax.tick_params(labelsize=14)

# Plot potential and wave functions and probability
# distributions. We normalize 

for i in range(nbound):
    fig, ax = plt.subplots()
    psi = v[:,i]                        # wave function psi
    psi = psi/(np.max(psi)-np.min(psi)) # normalize
    psi2 = psi**2                       # probability dens 
    psi2 = psi2/np.max(psi2)            # normalize
    ax.plot(x[1:n],psi,"r")
    ax.plot(x[1:n],psi2,"r--")
    title = ["n = ",str(i)]
    ax.set_title(" ".join(title),fontsize=14)
    ax.axis("off")