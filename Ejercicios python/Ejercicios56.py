# Programa que elimine espacios en blanco de caracteres
def eliminador_espacios(frase):
    return frase.replace(" ", "")
frase=str(input("ingrese la frase: "))
print(eliminador_espacios(frase))