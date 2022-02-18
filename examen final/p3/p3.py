# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:49:43 2022

@author: AMD
"""

# Dada la Lista [10,20,30,10,5, 1, 3, 5, 4] separar en dos listas de pares e impares
lista = [10,20,30,10,5, 1, 3, 5, 4]
listPares=[]
listImpares=[]
for num in lista:
    if num % 2 == 0:
        # es par
        listPares.append(num)
    else:
        listImpares.append(num)

print(lista)
print(listPares)
print(listImpares)