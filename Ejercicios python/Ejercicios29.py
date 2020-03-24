"""29.) Programa que visualice en pantalla los números múltiplos de 5
comprendidos entre 1 y 100"""
def multiplos():
    cont=0
    i=1
    while cont<100:
        cont=5*i
        i+=1
        print(cont)
multiplos()
