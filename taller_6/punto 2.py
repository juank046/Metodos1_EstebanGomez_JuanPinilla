#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:37:49 2022

@author: juancamilo
"""

import numpy as np
import matplotlib.pyplot as plt

class clase:
    def __init__(self,A,b):
        self.A=A
        self.b=b
    def GetJacobiMethod(self,itmax=1000,error = 1e-10):
        M,N = self.A.shape
        x = np.zeros(N)
        sumk = np.zeros_like(x)
        x = [13,20,-1]
        it = 0
        residuo = np.linalg.norm( self.b - np.dot(self.A,x) )
        while ( residuo > error and it < itmax ):
            it += 1
            for i in range(M):
                sum_ = 0
                for j in range(N):
                    if i != j:
                        sum_ += self.A[i][j]*x[j]
                        sumk[i] = sum_
            for i in range(M):
                if self.A[i,i] != 0:
                    x[i] = (self.b[i] - sumk[i])/self.A[i,i]
                else:
                    print('No invertible con Jacobi')
            residuo = np.linalg.norm( self.b - np.dot(self.A,x) )
        return x,it
    def Gauss(self,itmax=int(1e5),error = 1e-10):
        N=self.A.shape[0]
        xsol=np.zeros(N)
        res=1
        it=0
        while it<itmax and res>error:
            for i in range(N):
                sum_=0
                for j in range(N):
                    if j!=i:
                        sum_+=(-self.A[i][j]*xsol[j])
                sum_+=self.b[i]
                sum_/=self.A[i][i]
                xsol[i]=sum_
            res=np.linalg.norm(self.b-np.dot(self.A,xsol))
            it+=1
        return xsol,it
A=np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])
b=np.array([1.,3.,7.])
sistema=clase(A,b)
xJacobi,itJacobi=sistema.GetJacobiMethod()
xGauss,itGauss=sistema.Gauss()
print("La solución con Jacobi es: ",xJacobi," y sus iteraciones fueron: ",itJacobi)
print("La solución con GaussSidel es: ",xGauss," y sus iteraciones fueron: ",itGauss)