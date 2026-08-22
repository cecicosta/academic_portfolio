#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:05:28 2026

@author: cecilia.costa
"""

import sympy as  sym
import matplotlib.pyplot as plt
import numpy as np

Z = 1

# Define sympy expressions for radial functions
def P1s(r):
    k = 2
    exp = sym.exp(-Z*r)
    Zpwr = Z**(3/2)
    return k * Zpwr * r * exp

def P2s(r):
    k = sym.Rational(1/sym.sqrt(2)) * (1 - sym.Rational(1/2)*Z*r)
    exp = sym.exp(-Z*(r/2))
    Zpwr = (Z**(3/2)) 
    return k * Zpwr * r * exp

def P3s(r):
    k = sym.Rational(2/3)*(3**sym.Rational(-1/2)) * (1 - sym.Rational(2/3)*Z*r + sym.Rational(2/27)*(Z**2)*(r**2))
    exp = sym.exp(-Z*(r/3))
    Zpwr = (Z**(3/2)) 
    return k * Zpwr * r * exp


def P2p(r):
    k = sym.Rational(1/2)*6**sym.Rational(-1/2)
    exp = sym.exp(-Z*(r/2))
    Zpwr = (Z**(5/2)) 
    return k * Zpwr * (r**2) * exp

def P3p(r):
    k = sym.Rational(8/27)*6**sym.Rational(-1/2) * (1 - sym.Rational(1/6)*Z*r)
    exp = sym.exp(-Z*(r/3))
    Zpwr = (Z**(5/2)) 
    return k * Zpwr * (r**2) * exp

def P3d(r):
    k = sym.Rational(4/81)*30**sym.Rational(-1/2)
    exp = sym.exp(-Z*(r/3))
    Zpwr = (Z**(7/2)) 
    return k * Zpwr * (r**3) * exp


# Declare r symbol
r = sym.symbols("r")
labels = ["{1s}", "{2s}", "{3s}", "{2p}", "{3p}", "{3d}"]
i = 0
for Pnl in [P1s(r), P2p(r), P3s(r),P2p(r), P3p(r), P3d(r)]:
    
    # Convert sympy radial expression to lambda
    s = (r)
    pnl = sym.lambdify(s, Pnl, modules='numpy')
    
    label = sym.latex(Pnl)
    orbital = format(rf"P_{labels[i]} (r)")
    i = i + 1

    
    # Calculate the integral for the radial function 
    radialInt = sym.Integral(Pnl, (r, 0, sym.oo))
    radialIntValue = sym.integrate(Pnl, (r, 0, sym.oo))
    # Convert results to latex
    exprLatex = sym.latex(radialInt).replace("\limits_", "_")
    valueLatex = sym.latex(radialIntValue)
    radialLatexLine = rf"$\int_{0}^\infty {orbital} = {valueLatex}$"
    
    
    # Calculate the expectation for <r>
    integral = sym.Integral(r*Pnl**2, (r, 0, sym.oo))
    integral_value = sym.integrate(r*Pnl**2, (r, 0, sym.oo))
    # Convert results to latex
    exprLatex = sym.latex(integral).replace("\limits_", "_")
    valueLatex = sym.latex(integral_value)
    expectLatexLine = rf"$\langle r \rangle = {valueLatex}$"
    
    
    fig, ax = plt.subplots()
    
    # Plot radial function 
    ri = np.linspace(0, 40, 1000)
    ax.plot(ri, pnl(ri), label = rf"${orbital}$")
    ax.plot([0], [0], label = r"Radial Expectation:", color="white")
    ax.plot([0], [0], label = expectLatexLine, color="white")
    ax.plot([0], [0], label = "Radial Function integral:", color="white")
    ax.plot([0], [0], label = radialLatexLine, color="white")
    
    
    extratickes = [float(radialIntValue), float(integral_value)]
    ax.set_xticks(extratickes)
    
    # Create the dashed lines to highlght the target
    ax.vlines( extratickes[1] , 0 , pnl(extratickes[1]) , linestyle = "dashed" )
    #plt.hlines( target_y , 0 , target_x , linestyle = "dashed" )
    
        
    ax.legend(loc="upper right")
    plt.grid()
    plt.show()