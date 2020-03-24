#Calcule la suma de los números hasta un número dado por el usuario
def la_sumatoria(n):
    cont=0
    for i in range(n+1):
        cont+=i
    return cont
n=int(input("ingrese el numero: "))
print(la_sumatoria(n))