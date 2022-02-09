# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:29:53 2022

@author: AMD
"""

#Dada una cadena verificar que sea palindroma
comparar, aux = 0, 0
texto = input("Ingrese una palabra: ")
#metodo reversed permite invertir una lista sin modificarla 
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    comparar += 1
  aux += 1
if len(texto) == comparar:
  print("es palindromo")
else:
  print("no es palindromo")