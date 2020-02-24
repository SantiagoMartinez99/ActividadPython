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

#66.) Calcular factorial usando funciones
def factorial(numero):
    i=0
    for i in range(numero):
        i+=i*i
    return i