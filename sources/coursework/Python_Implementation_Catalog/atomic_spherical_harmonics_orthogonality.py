#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:03:23 2026

@author: cecilia.costa
"""


import sympy as  sym
import matplotlib.pyplot as plt

# =============================================================================
# Using SymPy functions to perform the integrations, verify that the spheri- 
# cal harmonics given on page 2 satisfy the following orthogonality relations
# =============================================================================


theta, phi = sym.symbols("\\theta \phi")

Y00 = sym.Function('Y_{00}')(theta, phi)
Y00_expr = lambda m_sign: 1/sym.sqrt(4*sym.pi)

Y11_plus = sym.Function('Y_{1+1}')(theta, phi)
Y11_minus = sym.Function('Y_{1-1}')(theta, phi)
Y11_expr = lambda m_sign: -m_sign * sym.sqrt(sym.Rational(3/8)/sym.pi) * sym.sin(theta) * sym.exp( m_sign * sym.I*phi)

Y10 = sym.Function('Y_{10}')(theta, phi)
Y10_expr = lambda m_sign: sym.sqrt(sym.Rational(3/4)/sym.pi) * sym.cos(theta) * sym.exp(2*sym.I*phi)

Y22_plus = sym.Function('Y_{2+2}')(theta, phi)
Y22_minus = sym.Function('Y_{2-2}')(theta, phi)
Y22_expr = lambda m_sign: sym.sqrt(sym.Rational(15/32)/sym.pi) * sym.sin(theta)**2 * sym.exp(m_sign * 2 * sym.I*phi)

Y21_plus = sym.Function('Y_{2+1}')(theta, phi)
Y21_minus = sym.Function('Y_{2-1}')(theta, phi)
Y21_expr = lambda m_sign: -m_sign*sym.sqrt(sym.Rational(15/8)/sym.pi) * sym.sin(theta)*sym.cos(theta) * sym.exp(m_sign * sym.I*phi) 

Y20 = sym.Function('Y_{20}')(theta, phi)
Y20_expr = lambda m_sign: sym.sqrt(sym.Rational(5/16)/sym.pi) * (2*sym.cos(theta)**2 - sym.sin(theta)**2)


# Now we try calculating the inner product between the functions
func_sym = [Y00, Y11_plus, Y11_minus, Y10, Y22_plus, Y22_minus, Y21_plus, Y21_minus, Y20]
func_expr = [Y00_expr(1), Y11_expr(1), Y11_expr(-1), Y10_expr(1), Y22_expr(1), Y22_expr(-1), Y21_expr(1), Y21_expr(-1), Y20_expr(1)]



for i in range(0, len(func_sym)):
    
    rows = len(func_sym) - i
    fig_height = 1 + 0.5 * rows

    fig, ax = plt.subplots(figsize=(14, fig_height))
    ax.axis("off")

    title = (
        rf"${sym.latex(func_sym[i])}$ Orthogonality check against:"
        "\n"
        rf"${sym.latex(func_sym[i:])}$"
        )
    
    ax.text(0.5, 1, title, ha="center", va="top", transform=ax.transAxes, fontsize=14)
    
    # Body text 
    y = 0.8 - i/(2*len(func_sym)) # try accounting for the image distortion with less rows
    dy = 0.75 / max(rows, 1)

    for j in range(i, len(func_sym)):
        # Calculate the double integral for the functional inner product
        integrand = sym.conjugate(func_expr[i]) * func_expr[j] * sym.sin(theta)
        integral = sym.Integral(integrand, (theta, 0, sym.pi), (phi, 0, 2*sym.pi))
            
        # Evaluate the expression
        integral_value = sym.integrate(integrand, (theta, 0, sym.pi), (phi, 0, 2*sym.pi))
        
        # Obtaine the inner product expression
        inner_product = format(r"\langle %s, %s \rangle" % (sym.latex(func_sym[i]), sym.latex(func_sym[j])))
        # Obtain the integral expression in latex
        integral_latex = sym.latex(integral)
        # Replace the latex expression \int_limits_{}^{} for the supported \int_{}^{}
        integral_latex = integral_latex.replace("\limits_", "_")
        
        print(integral_latex)
        print(integral_value)
        print(inner_product)
        
        line = rf"${inner_product} = {integral_latex} = {sym.latex(integral_value)}$"

        ax.text(
            0.05, y,
            line,
            ha="left",
            va="top",
            transform=ax.transAxes,
            fontsize=13
        )    
        y -= dy

    plt.show()
