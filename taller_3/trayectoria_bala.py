#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:10:45 2022

@author: juancamilo
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import wget
import os.path as path
file = 'Bala_Trayectoria.csv'
url = "https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv"
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    print('--File found---')
    Path_ = file
Data = pd.read_csv(Path_,sep=',')
X = np.float64(Data['X'])
Y = np.float64(Data['Y'])
def lagrange(x,xi,j):
    producto = 1.0
    n = len(xi)
    for i in range(n):
        if i != j:
            producto *= (x - xi[i])/(xi[j]-xi[i])
    return producto
def polinomio(x,xi,yi):
    suma = 0.
    n = len(xi)
    for j in range(n):
        suma += yi[j]*lagrange(x,xi,j)
    return suma
x = np.linspace(0,6,100)
y = polinomio(x,X,Y)
plt.scatter(X,Y,color='r')
plt.plot(x,y,color='k')
x=sym.Symbol("x")
f=polinomio(x,X,Y)
f=sym.expand(f)
g=9.8
theta1=np.arctan(0.363970234266202)
theta=round((theta1*180)/np.pi,2)
velocidad=round(np.sqrt(g/(0.0554912422401579*(np.cos(theta1)**2)*2)),2)
print("V=",velocidad,"m/sˆ2",";","theta=",theta)