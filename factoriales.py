#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:09:06 2022

@author: juancamilo
"""

def factorial(n:int):
    i=0
    fact=1
    while i<n:
        fact=fact*(n-i)
        i+=1
    return fact
lista=[]
i=0
while i<20:
    lista.append(factorial(i))
    i+=1
print(lista)
def variacion_sin_repeticion(n:int,r:int):
    resultado=(factorial(n))/(factorial(n-r))
    return int(resultado)
print(variacion_sin_repeticion(6, 3),"combinaciones")
def combinacion_sin_repeticion(n:int,m:int):
    resultado=(factorial(n))/((factorial(m))*factorial(n-m))
    return int(resultado)

print(combinacion_sin_repeticion(22,11), "cualquiera puede ser arquero")
print(combinacion_sin_repeticion(21,10), "ya sabemos quien es el arquero")

