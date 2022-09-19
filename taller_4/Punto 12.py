#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:36:31 2022

@author: juancamilo
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def funcion(x):
    return(1/(x**2))
a=1
b=2
Roots,Weights = np.polynomial.legendre.leggauss(2)
t = 0.5*((b-a)*Roots + a + b)
Integral = 0.5*(b-a)*np.sum( Weights*funcion(t) )
print("El resultado con 2 puntos es: ",Integral )
Roots,Weights = np.polynomial.legendre.leggauss(3)
t = 0.5*((b-a)*Roots + a + b)
Integral = 0.5*(b-a)*np.sum( Weights*funcion(t) )
print("El resultado con 3 puntos es: ",Integral )
