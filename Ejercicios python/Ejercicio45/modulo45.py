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

#45.
def matriz(ancho, largo):
    lista=[]
    matriz=[]
    for i in range(ancho):
        for i in range(largo):
            lista.append(rd.randint(0,100))
        matriz.append(lista)
        lista=[]
    maximo=matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]>maximo:
                maximo=matriz[i][j]
    print(matriz)
    return maximo
