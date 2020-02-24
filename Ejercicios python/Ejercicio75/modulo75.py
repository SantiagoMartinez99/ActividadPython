#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Santiago
#
# Created:     24/02/2020
# Copyright:   (c) Santiago 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#75.) Calcular la potencia de un numero usando recursividad
def potencia_recursivo(a,b):
    if b==0:
        return 1
    else:
        return a*potencia_recursivo(a,b-1)
