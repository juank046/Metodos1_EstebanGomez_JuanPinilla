#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:19:10 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt

def Gauss(A,b,itmax=int(1e5),error = 1e-10):
    N=A.shape[0]
    xsol=np.zeros(N)
    res=1
    it=0
    while it<itmax and res>error:
        for i in range(N):
            sum_=0
            for j in range(N):
                if j!=i:
                    sum_+=(-A[i][j]*xsol[j])
            sum_+=b[i]
            sum_/=A[i][i]
            xsol[i]=sum_
        res=np.linalg.norm(b-np.dot(A,xsol))
        it+=1
    return xsol,it
A=np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b=np.array([1.,3.,7.])
xsol,it=Gauss(A,b)
print("La solución es: " ,xsol," y sus iteraciones fueron: ",it )