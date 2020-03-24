
"""Programa que detecte dos números del teclado y si el primero es mayor que
el segundo intercambie sus valores"""
def mayor_menor(a,b):
    if a>b:
        print(b,a)
    else:
        print(a,b)
a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
mayor_menor(a,b)
