#66.) Calcular factorial usando funciones
def factorial(numero):
    fact=1
    i=1
    for i in range(1,numero+1):
        fact=fact*i
    return fact
numero=int(input("ingrese el numero"))
print(factorial(numero))