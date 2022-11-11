#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:47:28 2022

@author: juancamilo
"""


import numpy as np
import matplotlib.pyplot as plt
tienen_diario=np.array([-1,1])
tienen_cable=np.array([-1,1])
prob_diaro=np.array([0.4,0.6])
prob_cable=np.array([0.2,0.8])
uno=np.zeros(int(1e5))
solo_1=np.zeros(int(1e5))
for i in range(len(uno)):
    diario=np.random.choice(tienen_diario,p=prob_diaro)
    cable=np.random.choice(tienen_cable,p=prob_cable)
    if diario == 1 and cable==1:
        uno[i]=1
        solo_1[i]=0
    elif (diario==1 and cable==-1) or (diario==-1 and cable==1):
        uno[i]=1
        solo_1[i]=1
    else:
        uno[i]=0
        solo_1[i]=0
a,_,_=plt.hist(uno)
prob_uno=a[9]*100/int(1e5)
print("la probabilidad de que un residente tenga alguno de los 2 es: ",prob_uno)
b,_,_=plt.hist(solo_1)
prob_solo_1=b[9]*100/int(1e5)
print("la probabilidad de que un residente tenga solo 1 de los 2: ",prob_solo_1)
