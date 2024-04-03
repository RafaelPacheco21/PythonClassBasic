import math
#este es el código de nuestra funcion
def calcular_area_circulo(radio):
    area=math.pi*radio**2
    return area


#este es el codigo del programa, primero se ejecutara
radio=float(input('Escribe el radio del circulo y calcularrre su área'))
#aqui llamaremos a la funcion
areaCirculo=calcular_area_circulo
print('El área del circulo es:', round (areaCirculo,2))
