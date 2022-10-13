#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:16:34 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
G=(lambda x,y: np.log((x**2)+(y**2))-np.sin(x*y)-np.log(2)-np.log(np.pi), \
   lambda x,y: np.exp(x-y)+np.cos(x*y))
def GetVectorF(G,r):
    dim = len(G)
    v = np.zeros(dim)
    for i in range(dim):
        v[i] = G[i](r[0],r[1]) 
    return v
def GetJacobian(G,r,h=1e-6):
    dim = len(G)
    J = np.zeros((dim,dim))
    for i in range(dim):
        J[i,0] = (  G[i](r[0]+h,r[1]) - G[i](r[0]-h,r[1]) )/(2*h)
        J[i,1] = (  G[i](r[0],r[1]+h) - G[i](r[0],r[1]-h) )/(2*h)
    return J.T
def NewtonRaphson(G,r,error=1e-10):
    it = 0
    d = 1
    Vector_d = np.array([])
    while d > error:
        it += 1
        rc = r
        F = GetVectorF(G,r)
        J = GetJacobian(G,r)
        InvJ = np.linalg.inv(J)
        r = rc - np.dot( InvJ, F )
        diff = r - rc
        d = np.linalg.norm(diff)
        Vector_d = np.append( Vector_d , d )
    return r,it,Vector_d
def GetMetric(G,r):
    v = GetVectorF(G,r)
    return 0.5*np.linalg.norm(v)**2
def GetFig(F,R,it):
    fig = plt.figure(figsize=(8,4))
    labels = ['X','Y']
    ax = fig.add_subplot(1,2,1)
    ax1 = fig.add_subplot(1,2,2)
    ax.set_title('Metric: %.20f' %(F[it]))
    ax.plot(F[:it])
    ax.set_xlabel('%.0f' %(it))
    ax.set_yscale('log')
    ax1.plot(R[:it],label=labels)
    ax1.set_xlabel('%.0f' %(it))
    ax1.legend(loc=0)
    plt.show()
def GetSolve(G,r,lr=1e-3,epochs=int(1e5),error=1e-7):
    d = 1
    it = 0
    Vector_F = np.array([])
    R_vector = np.array(r)
    while d > error and it < epochs:
        CurrentF = GetMetric(G,r)
        J = GetJacobian(G,r)
        GVector = GetVectorF(G,r)
        r -= lr*np.dot(J,GVector) 
        R_vector = np.vstack((R_vector,r))
        NewF = GetMetric(G,r)
        Vector_F = np.append(Vector_F,NewF)
        d = np.abs( CurrentF - NewF )/NewF
        if it%500 == 0:
            clear_output(wait=True)
            GetFig(Vector_F,R_vector,it)
            time.sleep(0.01)
        it += 1
    if d < error:
        print(' Entrenamiento completo ', d, 'iteraciones', it)
    if it == epochs:
        print(' Entrenamiento no completado ')
    return r,it,Vector_F,R_vector
r,it,distancias = NewtonRaphson(G,[2,2])
print("Respuesta con NewtonRaphson: ",r)
xsol,it,F,R = GetSolve(G,[2,2])
print("Respuesta con decenso: ",xsol)
    
    
    
    
    
    
    
    