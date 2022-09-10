#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:31:34 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import wget
import os.path as path
file = 'Newton.csv'
url = "https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv"
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    print('--File found---')
    Path_ = file
Data = pd.read_csv(Path_,sep=',')
X = np.float64(Data['X'])
Y = np.float64(Data['Y'])
def newton_gregory(X,Y,x):
    suma_ = Y[0]
    matriz = np.zeros((len(X),len(Y)))
    matriz[:,0] = Y
    for i in range(1,len(X)):
        for j in range(i, len(Y)): 
            matriz[j,i] = matriz[j,i-1]-matriz[j-1,i-1]
            matriz[j,i] = matriz[j,i]/(X[j]-X[j-i])
        polinomio = 1.0
        for k in range(0,i):
            polinomio*=(x-X[k])
        suma_ += polinomio*(matriz[i,i])
    return suma_
x = np.linspace(np.min(X),np.max(X),100)
y= newton_gregory(X,Y,x)
plt.scatter(X,Y,color='r')
plt.plot(x,y)
x=sym.Symbol("x")
f=newton_gregory(X, Y, x)
f=sym.expand(f)
print("polinomio=",f)