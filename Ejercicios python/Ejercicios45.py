import random as rd
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
ancho=int(input("ingrese el ancho: "))
largo=int(input("ingrese el largo: "))
print(matriz(ancho,largo))
