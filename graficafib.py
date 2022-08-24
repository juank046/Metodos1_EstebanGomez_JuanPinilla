# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 22:20:10 2022

@author: Esteban Gomez
"""

import fibonacci as fi
import matplotlib.pyplot as plt 

def grafica():
    plt.plot(fi.fibonacci(20), label="serie fibonacci")
    plt.legend(loc="upper left")
    plt.title("Grafica Fibonacci primeros 20 números")
    plt.show()
    
grafica()