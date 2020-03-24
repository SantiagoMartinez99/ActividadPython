#76.) Calcular factorial usando recursividad
def factorial_recursivo(numero):
    if(numero==0):
        return 1
    else:
        return numero*factorial_recursivo(numero-1)
numero=(int(input("ingrese el numero:")))
print(factorial_recursivo(numero))