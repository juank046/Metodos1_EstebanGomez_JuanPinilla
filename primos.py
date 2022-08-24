#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 11:35:05 2022

@author: juancamilo
"""



def es_primo(numero: int)->bool:
    i=1
    div=0
    res=False
    while i<=numero:
        if numero%i==0:
            div+=1
        i+=1
    if div==2:
        res=True
        
    return res

def primeros_primos():
    i=2
    lista=[]
    while len(lista) <= 999:
        if es_primo(i)==True:
            lista.append(i)
        i+=1
    return lista

lista = primeros_primos()
print(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8],lista[9])
import matplotlib.pyplot as plt
def grafica():
    plt.plot(lista)
    plt.show
grafica()