# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:04:26 2022

@author: Esteban Gomez
"""
#punto 4

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


puntos = np.random.uniform(0,1,size=int(10e5))
N = int(10e4)
x = np.arange(1,30,1)
correlaciones = []

def test(puntos, N, x):
    count = 0 
    for i in range(N):
        count += puntos[i] * puntos[i+x]
   
    return count/N

for i in range(len(x)):
    correlaciones.append(test(puntos, N, x[i]))
    
print(correlaciones)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(1,1,1)
ax.plot(x,correlaciones,color='b')
ax.set_ylim((0.2,0.3))
plt.show()