#crearemos una super clase llamada figura, con un atributo color y 
#un método dibujar
class Figura:
    def __init__(self, color):
        self.color=color
    
    def dibujar (self):
        print(f'Estamos dibujando una figura de color: {self.color}') 
#crearemos una subclase llamada Rectangulo que hereda de figura 
class Rectangulo (Figura):
    def __init__(self, color, ancho,alto):
        super().__init__(color)
        self.ancho=ancho
        self.alto=alto
    
    def calcular_area(self):
        return self.alto*self.ancho
#crearemos una subclase llamada Circulo que hereda de figura 
class Circulo (Figura):
    def __init__(self, color, radio): 
        super().__init__(color) 
        self.radio-radio
    
    def calcular_area(self):
        return 3.14*(self.radio**2)
#construiremos los objetos
miRectangulo=Rectangulo ('Azul',9,17)
micirculo=Circulo ('Amarillo',13)
#usaremos los métodos del objeto miRectángulo 
miRectangulo.dibujar()
print('La figura es de tipo rectangulo')
print('El color de la figura es: ',miRectangulo.color)
print('El area del rectangulo es: ',miRectangulo.calcular_area())
#usaremos metodos y atributos del objeto miCirculo
micirculo.dibujar()
print('La figura es de tipo Circulo')
print('El color de la figura es: ', micirculo.color)
print('El area del circulo es: ',micirculo.calcular_area())