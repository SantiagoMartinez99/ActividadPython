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

"""86.) Escribir un programa que escriba la lista de caracteres ASCII dentro de un
archivo detexto."""
def archivo_ascii():
    archivo= open('caracteres.txt','w')
    with open("caracteres.txt","w"):
        for i in range(0,50):
            numero=rd.randint(0,50)
            numero2=chr(numero)
            i+=1
            archivo.write(numero2)