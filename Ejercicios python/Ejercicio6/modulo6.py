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
import math as mt
#6.) Longitud y area de una circunferencia
def area_circunferencia(r):
    area1=mt.pi*r**2
    perimetro=2*mt.pi*r
    return area1, perimetro