#Solicite cinco numeros y calcular la media aritmetica
def media_aritmetica():
    lista=[]
    for i in range(5):
        lista.append(int(input("Ingrese un numero: ")))
    cont=0
    for valor in lista:
        cont+=valor
    return cont/len(lista)
print(media_aritmetica())
