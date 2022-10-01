#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:30:57 2022

@author: juancamilo
"""

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from mpl_toolkits.mplot3d import axes3d

def CreateCircle( N, R ):
    X = np.zeros(N)
    Y = np.zeros_like(X)
    Z = np.zeros_like(X) 
    for i in tqdm(range(N)):
        rho=(np.random.uniform(0,R))
        rho=rho**(1/3)
        cosphi = np.random.uniform(-1,1)
        phi=np.arccos(cosphi)
        theta = np.random.uniform(0,2*np.pi)
        X[i] = rho*np.sin(phi)*np.cos(theta)
        Y[i] = rho*np.sin(phi)*np.sin(theta)
        Z[i] = rho*np.cos(phi)
    return X,Y,Z
def funcion(X,Y,Z):
    return np.exp(np.sqrt((X**2)+(Y**2)+(Z**2)))
def integral(X,Y,Z,f):
    valores=np.array([])
    for i in tqdm(range(len(X))):
        valores=np.append(valores,f(X[i],Y[i],Z[i]))
    return (np.average(valores))*(4/3)*np.pi
X,Y,Z=CreateCircle(10000,1)
integralmc=integral(X, Y, Z, funcion)
print("El valor de la integral por montecarlo es: ",integralmc)
print("El valor real de la integral es: ", np.pi*4*(np.e-2))
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.view_init(10, 60)
ax.scatter(X,Y,Z,color='b')