# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:59:59 2022

@author: Esteban Gomez
"""

#Punto 3 multiplicacion de matrices 

import numpy as np 
#Comprobamos que el numero de columnas coincida con las filas 
def producto(A,B):
    fila_1 = len(A)
    Columna_1 = len(A[0])
    fila_2 = len(B)
    Columna_2 = len(B[0])
    if fila_1 != Columna_2:
        res = "El producto de matrices no se puede hacer"
        return res
    
    matriz = []
    #Creamos la matriz donde vamos a colocar el producto 
    for i in range(fila_2):
        matriz.append([])
        for j in range(Columna_2):
            matriz[i].append(0)
    
    
    
    
    #Hacemos la operacion 
    for x in range(Columna_2):
        for z in range(fila_1):
            prod = 0
            for y in range(Columna_1):
                prod += A[x][y]*B[y][x]
            matriz[z][x] = prod
    return matriz

A = [[1,0,0],[5,1,0],[-2,3,1]]
B = [[4,-2,1],[0,3,7],[0,0,2]]

Mat = producto(A, B)

    
    
   
    