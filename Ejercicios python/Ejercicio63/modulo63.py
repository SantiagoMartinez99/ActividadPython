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

#63.)
def palindromo(palabra):
    lista=[]
    palabra.strip(" ")
    if palabra[:]==palabra[::-1]:
        return True
    else:
        return False