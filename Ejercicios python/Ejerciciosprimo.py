#
def primo(numero):
    if numero<1:
        return "no es primo"
    elif numero==2:
        return "es primo"
    else:
        for i in range (2,numero):
            if numero % i == 0:
                return "no es primo"
            else:
                return "es primo"
numero=(int(input("ingrese el numero:")))
print(primo(numero))