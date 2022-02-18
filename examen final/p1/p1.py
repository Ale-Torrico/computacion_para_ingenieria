# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:20:13 2022

@author: AMD
"""

#Dada una cadena verificar que sea palindroma

igual, aux = 0, 0
texto = input("Ingrese una palabra: ")
#metodo reversed permite invertir una lista sin modificarla 
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("es palindromo!")
else:
  print(" no es palindromo!")
  
  