
#Area y perimetro circunferencia
import math as mt
def area_circunferencia(radio):
    area=mt.pi*(radio**2)
    perimetro=2*mt.pi*radio
    return (area, perimetro)
radio=int(input("ingrese el radio de la circunferencia: "))
area,perimetro=area_circunferencia(radio)
print("el area de la circunferencia es: "+str(area))
print("la longitud de la circunferencia es:"+str(perimetro))
