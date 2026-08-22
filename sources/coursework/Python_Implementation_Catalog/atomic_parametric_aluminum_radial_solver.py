# Program radiallog.py
# Program for solving the radial Schrödinger equation for a Coulomb potential V(r)=-Z/r and a
# given quantum number l. A transformation to logaritmic grid is done to increase numerical
# accuracy. A specific solution is targeted by giving the principal quantum number n.
# Jörgen Ekman and Per Jönsson, April 2015
# Matlab to python conversion by Asimina Papoulia and Wenxian Li, September 2020

import math
import numpy as np
import matplotlib.pyplot as plt
import sys


def Settings_Al_III():
    # Program settings fot Al III
    referenceStates = {
        "3s": (3, 0, 0),
        "3p": (3, 1, 53682.93),
        "3d": (3, 2, 115956.21),
        "4s": (4, 0, 126164.05),
        "4p": (4, 1, 143633.38),
        "4d": (4, 2, 165786.32),
        "4f": (4, 3, 167612.75),
        "5s": (5, 0, 170637.35)
        }
    Z = 13
    N = 11
    # List of states to calculate
    states = ["2p^6 3s^1", "2p^6 3p^1", "2p^6 3d^1", "2p^6 4s^1", "2p^6 4p^1", "2p^6 4d^1", "2p^6 4f^1", "2p^6 5s^1"]
    return (referenceStates, N, Z, states)

def Settings_Na_I():
    # Settings for Na I
    referenceStates = {
        "3s": (3, 0, 0),
        "3p": (3, 1, 16956.17025),
        "4s": (3, 2, 25739.999),
        "3d": (4, 0, 29172.837),
        "4p": (4, 1, 30266.99 ),
        "5s": (4, 2, 33200.673),
        "4d": (4, 3, 34548.729),
        "4f": (5, 0, 34586.92)
        }
    Z = 11
    N = 11
    states = ["2p^6 3s^1", "2p^6 3p^1", "2p^6 4s^1", "2p^6 3d^1", "2p^6 4p^1", "2p^6 5s^1", "2p^6 4d^1", "2p^6 4f^1"]
    return (referenceStates, N, Z, states)

def Settings_Li_I():
    # Settings for Li I
    referenceStates = {
        "2s": (2, 0, 0),
        "2p": (2, 1, 14903.66 ),
        "3s": (3, 0, 27206.12),
        "3p": (3, 1, 30925.38 ),
        "3d": (3, 2, 31283.08),
        "4s": (4, 0, 35012.06),
        "4p": (4, 1, 36469.55),
        "4d": (4, 2, 36623.38)
        }
    Z = 3
    N = 3
    states = ["1s^2 2s^1", "1s^2 2p^1", "1s^2 3s^1", "1s^2 3p^1", "1s^2 3d^1", "1s^2 4s^1", "1s^2 4p^1", "1s^2 4d^1"]
    return (referenceStates, N, Z, states)

    

def AUnitToSpectroscopic(E):
    return E*219474.63

def parametricPotential(r, Z, N, param):
    return -Z/r +  ((N - 1)*r)/(param**2 + r**2) 


def radiallog(n,l, N, Z, param, plot=True):


    if Z > 0 and l < n:
        E = -Z**2 / 2  # starting energy taken as the lowest possible
        nodes = n - l - 1  # targeted number of nodes
    else:
        sys.stderr.write('Invalid input\n')
        sys.exit(-1)

    rhomin = -10
    h = 1 / 48  # step size

    nodes_count = -1  # initial values of nodes
    dE = math.inf  # initial values of difference of derivat at r_c
    E_upper = -2.0e-52  # initial values of upper bound of energy during iter
    E_lower = -math.inf  # initial values of lower bound of energy during iter
    num_iter = 0

    while nodes != nodes_count or abs(dE) > 1.0e-10:
        # Make sure that the energy is such that the turning point is in the interior of the grid
        while 1:
            r_inf = 40 / math.sqrt(2 * abs(E))  # practical infinity
            rhoi = math.log(Z * r_inf)  # practical infinity in rho
            grid_points = round((-rhomin + rhoi) / h)  # number of grid points
            rho = rhomin + np.linspace(0, grid_points - 1, grid_points) * h  # generate grid
            r = np.exp(rho) / Z

            # Define the effective potential
            U = np.linspace(0, 0, grid_points)
            U[0] = 0  # initialize U, gets a 0 value at r = 0
            U[1:] = parametricPotential(r[1:], Z, N, param) + l * (l + 1) / (2 * r[1:]**2)
#            U[1:] = -Z / r[1:] + l * (l + 1) / (2 * r[1:]**2)

            # Determine the outer classical turning point. Start from the practical infinity
            # and step inwards until U(i) < E
            i_c = grid_points - 1

            for i in range(grid_points - 1, -1, -1):
                if U[i] < E:
                    i_c = i
                    break

            # If turning point not in the interior increase the energy and try again
            if i_c == grid_points - 1:
                E = 0.9 * E
            else:
                break

        g = -2 * r**2 * (E - parametricPotential(r, Z, N, param)) + (l + 1 / 2)**2
        alpha = 1 - (h**2 / 12) * g  # alpha and g function for Numerow
        beta = 2 + (5 * h**2 / 6) * g  # beta for Numerov's method

        # Perform the outward integration
        P_out = np.zeros(grid_points)  # initialize P_out
        P_out[0] = r[0]**(l + 1) * (1 - Z * r[0] / (l + 1)) / math.sqrt(r[0])  # starting values from regular
        P_out[1] = r[1]**(l + 1) * (1 - Z * r[1] / (l + 1)) / math.sqrt(r[1])  # solution at r = 0

        for i in range(1, i_c + 1):
            P_out[i + 1] = (beta[i] * P_out[i] - alpha[i - 1] * P_out[i - 1]) / alpha[i + 1]

        # Perform the inward integration
        P_in = np.zeros(grid_points)  # initialize P_in

        # starting values from regular solution at r_inf
        P_in[grid_points - 1] = np.exp(-np.sqrt(2 * abs(E) * r[grid_points - 1])) / math.sqrt(r[grid_points - 1])
        P_in[grid_points - 2] = np.exp(-np.sqrt(2 * abs(E) * r[grid_points - 2])) / math.sqrt(r[grid_points - 2])

        for i in range(grid_points - 2, i_c - 1, -1):
            P_in[i - 1] = (beta[i] * P_in[i] - alpha[i + 1] * P_in[i + 1]) / alpha[i - 1]

        # Scale and merge solutions
        P_out = P_out / P_out[i_c]
        P_in = P_in / P_in[i_c]
        P = np.append(P_out[0:i_c], P_in[i_c:])

        # Count the number of nodes. At a node position, P(i+1)P(i) is negative
        nodes_count = 0

        for i in range(1, grid_points - 1):
            if P[i + 1] * P[i] < 0:
                nodes_count += 1

        # Check nodes and adjust E
        if nodes_count > nodes:
            E_upper = min(E_upper, E)

            if E * 1.1 < E_lower:
                E = (E_lower + E) / 2
            else:
                # too many nodes, decrease E
                E = E * 1.1

        elif nodes_count < nodes:
            E_lower = max(E_lower, E)

            if E * 0.9 > E_upper:
                E = (E + E_upper) / 2
            else:
                # too few nodes, increase E
                E = E * 0.9

        # Fine tune the energy
        if nodes_count == nodes:
            # Compute the derivatives and take difference
            DP_out = (P_out[i_c + 1] - P_out[i_c - 1]) / (2 * h)
            DP_in = (P_in[i_c + 1] - P_in[i_c - 1]) / (2 * h)
            dE = (DP_out - DP_in) * P[i_c] / (2 * sum(r**2 * P**2) * h)

            # Damp if step is too large
            while E + dE > 0:
                dE = dE / 2

            E = E + dE


        num_iter += 1

    # Normalize and check slope
    norm = math.sqrt(sum(P**2 * r**2) * h)
    P = P / norm

    if P[1] < 0:
        P = -P

    # Compute radial expectation value
#    r1 = sum(r**3 * P**2) * h

#    endtime = datetime.datetime.now().timestamp()
#    print("time used: %f s" % (endtime - starttime))

    # Write energy and plot solution
#    print("Number of iterations: %d" % (num_iter,))
#    print("Nodes: %d" % (nodes_count))
#    print("Number of grid points: %d" % (grid_points,))
#    print("Energy eigenvalue: %.16e a.u.." % (E,))
#    print("Radial expectation value: %.16e a.u." % (r1,))

    orbital = ["s", "p", "d", "f", "g", "h", "i"]

    if plot:
        plt.figure()

        plt.subplot(211)
        plt.plot(r, np.sqrt(r) * P)
        plt.xlabel("r (a.u.)")
        plt.title("radial function for %d%s of Z = %d" % (n, orbital[l], Z,))
        plt.ylabel("P")

        rr = np.sqrt(r)

        plt.subplot(212)
        plt.plot(rr, np.sqrt(r) * P)
        plt.xlabel('$\sqrt{\mathrm{r}}$ (a.u.)')
        plt.ylabel("P")

        plt.tight_layout(pad=1.0)
        plt.show()

    return (r, P, E)


# =============================================================================
# The ground congura- tion is 1s22s22p63s and the excited congurations are given by 1s22s22p63p,
# 1s22s22p63d etc
# =============================================================================

def CalculateState(nl, N, Z, param):

    plt.figure(figsize=(12, 9), dpi=200)
    plt.suptitle(r"Orbital plots", fontsize=24)

    results = []

    letters = {0: "s", 1: "p", 2: "d", 3: "f"}

    for (n, l) in nl:

        r, P, E = radiallog(n, l, N, Z, param, False)
        results.append((r, P, E))

        label = f"{n}{letters[l]}"

        # Top plot

        plt.subplot(211)

        plt.plot(
            r,
            np.sqrt(r) * P,
            linewidth=1.0,
            label=label
        )

        plt.xlim(0, 80)
        plt.ylim(-1, 1)


        plt.xlabel("r (a.u.)", fontsize=18)
        plt.ylabel(r"$\sqrt{r}P(r)$", fontsize=18)

        plt.legend(
            loc="upper center",
            ncols=6,
            fontsize=18,
            frameon=False
        )

        # Bottom plot

        rr = np.sqrt(r)

        plt.subplot(212)

        plt.plot(
            rr,
            np.sqrt(r) * P,
            linewidth=1.0,
            label=label
        )

        plt.xlim(0, 8)

        plt.xlabel(r"$\sqrt{r}$ (a.u.)", fontsize=18)
        plt.ylabel(r"$\sqrt{r}P(r)$", fontsize=18)

        plt.legend(
            loc="upper center",
            ncols=6,
            fontsize=18,
            frameon=False
        )

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    plt.show()

    return results


def FindAlphaParameter(Eref, N, Z):
    levels = []
    alpha = 0.1
    alphaLast = alpha 
    meanERef = 0
    meanDeltE = 0
    error = np.inf
    
    for (n, l, dltaE) in list(Eref.values()):      
        E = radiallog(n, l, N, Z, alpha, False)[2]
        E = AUnitToSpectroscopic(E)
        levels.append(E)
        # Calculate the mean of the reference values
        meanERef = meanERef + dltaE/len(Eref.values())
    meanDeltE = (np.array(levels) - levels[0]).mean()

    error = meanERef - meanDeltE    

    # Look for a better value for alpha until the error is less than the arbitrary tolerance
    while(abs(error) > 100):
        # Adjust the parameter in the contrary direction to the error, relative to the mean of the reference values
        alpha = alpha + alpha*(-error)/abs(meanERef)
        
        # Reset values for new round
        levels = []
        alphaLast = alpha

        for (n, l, dltaE) in list(Eref.values()):      
            E = radiallog(n, l, N, Z, alpha, False)[2]
            E = AUnitToSpectroscopic(E)
            levels.append(E)
        meanDeltE = (np.array(levels) - levels[0]).mean()

        # If we obtained some improvement on this round, we update the parameter and try again   
        error = meanDeltE - meanERef   

        
    # The last update to the parameter made the error worse, so we rollback the change
    alpha = alphaLast
    return alpha
    

if __name__ == '__main__':
    
    (referenceStates, N, Z, states) = Settings_Li_I()
    

    # Calculate alpha for the parametric potential
    alpha = FindAlphaParameter(referenceStates, N, Z)
    print("Optimized value for alpha: %f" %alpha)
    
    nl = {
        "1s": (1, 0),
        "2s": (2, 0),
        "2p": (2, 1),
        "3s": (3, 0),
        "3p": (3, 1),
        "3d": (3, 2),
        "4s": (4, 0),
        "4p": (4, 1),
        "4d": (4, 2),
        "4f": (4, 3),
        "5s": (5, 0)
    }
    levels = CalculateState(list(nl.values()), N, Z, alpha)

    for i in range(0, len(nl)):
        print("Energy for level %s: %.16e a.u." %(list(nl.keys())[i], levels[i][2]))

    Energies = []    
    for s in states:
        E = 0
        orbitals = s.split(' ')
        for o in orbitals:
            orbital, electrons = o.split('^')
            index = list(nl.keys()).index(orbital)
            E = E + levels[index][2] * int(electrons)
        Energies.append(E)
        print(fr"DltaE_{orbitals}=%f cm^-1" %(AUnitToSpectroscopic(E - Energies[0])))
        
        

    
   