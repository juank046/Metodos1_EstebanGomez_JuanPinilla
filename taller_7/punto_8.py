#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:57:13 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

M = [[3,1,-1],[1,2,0],[0,1,2],[1,1,-1]]
t = [-3,-3,8,9]
M = np.array(M)
AT = np.dot(M.T,M)
bT = M.T @ t
xsol = np.linalg.solve(AT,bT)
proy = np.dot(M,xsol)

u1 = np.array([3,1,0,1])
u2 = np.array([1,2,1,1])
u3 = np.array([-1,0,2,-1])

v1 = u1
v1 = v1/np.linalg.norm(v1)
v2 = u2 - (np.dot(u2,v1)/(np.linalg.norm(v1)**2))*v1
v2 = v2/np.linalg.norm(v2)
v3 = u3 - (np.dot(u3,v1)/(np.dot(v1,v1)))*v1 - (np.dot(u3,v2)/(np.dot(v2,v2)))*v2
v3 = v3/np.linalg.norm(v3)

c1 = np.dot(t,v1)
c2 = np.dot(t,v2)
c3 = np.dot(t,v3)

proyeccion_b = c1*v1 + c2*v2 + c3*v3
print(proyeccion_b)
    