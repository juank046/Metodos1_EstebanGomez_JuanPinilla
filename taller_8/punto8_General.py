# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 08:40:31 2022

@author: Esteban Gomez
"""

#Ejercicio 8 

import random


conteo = 0
Total = 0

for i in range(int(10e4)):
    m1=random.choice([-1,1])
    m2=random.choice([-1,1])
    m3=random.choice([-1,1])
    m4=random.choice([-1,1])
    total = m1+m2+m3+m4
    if total == 0:
        conteo += 1
        Total += 1
    else:
        Total += 1

print(conteo)
print(Total)