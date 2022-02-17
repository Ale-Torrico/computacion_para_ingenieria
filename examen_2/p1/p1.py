# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:31:12 2022

@author: AMD
"""

#Crear un programar GUI que verifique que una palabra es palindroma

from tkinter import *
igual, aux = 0, 0
Label(texto = input("Ingrese una palabra: "))
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  Label(print("es palindromo!"))
else:
  Label(print("no es palindromo!"))
dow.mainloop