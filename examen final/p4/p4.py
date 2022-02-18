# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 09:43:27 2022

@author: AMD
"""

# Dada la lista [10,20,30,10,5, 1, 3, 5, 4] hacer un programa GUI que muestre un Listbox
# de los valores originales, un Listbox de Impares otra Listbox de Pares

from tkinter import *

listas=[10,20,30,10,5,1,3,5,4]
lista_pares= []
lista_impares= []
for num in listas:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
        
label_lista_pares= Label(window, text="los numeros pares son:")
label_lista_impares=label(window,text= "los numeros impares son ")
label_res=Label(window, text="<<los pares e impares son>>")


label_lista_pares.place(x=20, y=100)
input_lista_pares.place(x=200, y=10)

label_lista_impares.place(x=20, y=100)
input_lista_impares.place(x=200, y=10)

label_res.place(x=210, y = 100 )
buton_res.place(x=210, y = 110)


dow.mainloop()