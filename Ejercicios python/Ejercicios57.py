#Programa que determine palindromos
def palindromo(palabra):
    lista=[]
    palabra.strip(" ")
    if palabra[:]==palabra[::-1]:
        return True
    else:
        return False
palabra=str(input("ingrese la frase"))
print(palindromo(palabra))
