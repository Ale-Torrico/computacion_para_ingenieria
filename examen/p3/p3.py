# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:43:59 2022

@author: AMD
"""

#Dado el archivo estudiantes.txt y notas.txt unir en un solo archivo
# llamado primer_parcial.txt que contendra los nombre seguido de su nota.
f = open("estudiantes.txt", "r")
g = open ("notas.txt", "r")
c = open('texto 3.txt', 'w')

while(True):
    linea = f.readline()
    linea2 = g.readline()
    
    if not linea:
   
        break
    c.write(linea+ linea2 )
try:
    # Procesamiento para escribir en el fichero
    c.write(linea)
finally:
 
    c.close()
       
f.close()
g. close()


