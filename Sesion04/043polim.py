#crearemos clases con objetos diferentes 
class Circulo:
    def __init__(self,radio): 
        self.radio=radio
    
    def area(self):
        return 3.14* (self.radio**2)

class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto=alto
        self.ancho=ancho

    def area(self):
        return self.alto*self.ancho
    
class Triangulo:
    def __init__(self, base, altura): 
        self.base=base
        self.altura=altura
    
    def area(self):
        return (self.base*self.altura)/2

#crearemos una función que reciba objetos y verifique si tiene el método 
#area y lo ejecuten, en caso contrario avisará un error
#esta función pertenece al programa principal
def calcularArea(objeto):
    if hasattr(objeto, 'area'):
        return objeto.area()
    else:
        raise TypeError('El objeto no tiene un método area() válido')

#comienza el programa principal
circulo=Circulo(21)
rectangulo=Rectangulo(15,23)
triangulo=Triangulo(7,13)
#invocaremos los métodos de cada objeto a través de la funcion calcularArea 
print('El área del circulo es:', calcularArea(circulo))
print('El área del Rectángulo es:', calcularArea (rectangulo))
print('El áres del Triangulo es:', calcularArea(triangulo))