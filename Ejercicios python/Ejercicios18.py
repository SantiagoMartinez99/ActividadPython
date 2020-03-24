
#Detectar si un numero leido es par o impar
def par_o_impar(n):
    numero=n%2
    if numero==0:
        return "par"
    else:
        return "impar"
n=int(input("ingrese el numero: "))
print(par_o_impar(n))
