#crearemos la clase Triangulo con un método para calcular su área 
class Triangulo:
    def __init__(self,base, altura):
        self.base=base
        self.altura=altura
    def area(self):
        return(self.base* self.altura)/2
#pediremos los datos necesarios para crear el objeto de clase Triangulo
base=float(input('Escribe la base del Triangulo: '))
altura=float(input('Ahora escribe la altura del Triangulo: '))
#construiremos el objeto
triangulo=Triangulo (base, altura)

#invocaremos el método para calcular el área 
print('El área del triangulo es: ',triangulo.area())

#encapsulamiento
_dato=0 #prioridad máxima la variable es protegida NO TOCAR
_dato2=0 #prioridad media la variable es privada CUIDADO AL TOCAR
dato3=0 #prioridad baja o normal la variable es publica USALA COMO QUIERAS