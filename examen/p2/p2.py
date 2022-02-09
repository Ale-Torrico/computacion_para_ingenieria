# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:33:20 2022

@author: AMD
"""

# Dada la lista [10,20,30,10,5, 1, 3, 5, 4] separar en dos listas 
# una lista debe contener solo los pares y la segunda lista solo debe contener los impares
lista = [10,20,30,10,5, 1, 3, 5, 4]
Pares=[]
Impares=[]
for num in lista:
    if num % 2 == 0:
    
        Pares.append(num)
    else:
        Impares.append(num)

print(lista)
print(Pares)
print(Impares)
