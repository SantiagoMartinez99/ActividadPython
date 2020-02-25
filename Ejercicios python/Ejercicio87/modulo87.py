#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Santiago
#
# Created:     24/02/2020
# Copyright:   (c) Santiago 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""87.)Escribir un programa que lea y muestre en pantalla el archivo generado
en el ejercicio anterior."""
def lector_ascii():
    archivo= open('caracteres.txt','r')
    with open('caracteres.txt','r') as reader:
        for line in reader:
            return line
