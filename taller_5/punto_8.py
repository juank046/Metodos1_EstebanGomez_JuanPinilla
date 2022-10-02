
"""
Created on Thu Sep 29 20:32:34 2022

@author: Esteban Gomez
"""

#punto 8 

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
import sympy as sym


N=1000
x = np.random.uniform(0,1,size=int(N))
W=2
Z=4
lista = []
def fun(W,Z, x):
    funcion=factorial((W+Z)-1)/(factorial(W-1)*factorial(Z-1))*(x**(W-1))*(1-x)**(Z-1)
    return funcion 

f = fun(W,Z,x)
y = np.random.uniform(0,max(f), size = int(N))
contador = 0
for i in range(N):
    if y[i]<fun(W,Z,x[i]):
        lista.append(x[i])
        contador+=1

lista = np.array(lista)

x_ = fun(W,Z,x)
A = max(f)*contador/N

incertidumbre = 1/np.sqrt(N)*100

plt.scatter(x,x_)