# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 20:40:57 2022

@author: Esteban Gomez
"""

#fibonacci 
def fibonacci(n=int):
    cero = 0
    primer = 1
    contador = 0
    respuesta = 0
    lista = []
    while contador != n: 
        lista.append(cero)
        respuesta = cero + primer 
        cero = primer 
        primer = respuesta 
        contador +=1 
    return lista
        
print(fibonacci(20))
#numero aureo
