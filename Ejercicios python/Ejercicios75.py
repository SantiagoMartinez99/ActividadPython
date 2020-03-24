#75.) Calcular la potencia de un numero usando recursividad
def potencia_recursivo(a,b):
    if b==0:
        return 1
    else:
        return a*potencia_recursivo(a,b-1)
a=int(input("ingrese la base:"))
b=int(input("ingrese el exponente:"))
print(potencia_recursivo(a,b))