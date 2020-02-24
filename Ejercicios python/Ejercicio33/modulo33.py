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

#33.) Calcule la suma de los números hasta un número dado por el usuario
def la_sumatoria(n):
    cont=0
    for i in range(n+1):
        cont+=i
    return cont