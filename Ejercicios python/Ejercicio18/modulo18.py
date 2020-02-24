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
#18.) Detectar si un numero leído es par o impar
def par_o_impar(n):
    numero=n%2
    if numero==0:
        return "par"
    else:
        return "impar"
