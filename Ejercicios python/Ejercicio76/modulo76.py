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

#76.) Calcular factorial usando recursividad
def factorial_recursivo(numero):
    if(numero==0):
        return 1
    else:
        return numero*factorial_recursivo(numero-1)