#crearemos una clase que manipula información de vehiculos 
#usaremos un método para imprimir su ficha técnica

class Vehiculo:
    def __init__(self, marca, tipo, modelo, color):
        self.marca=marca
        self.tipo=tipo 
        self.modelo=modelo
        self.color=color
    #fichaTecnica camel Case
    def ficha_tecnica (self): #snake case
        print('---FICHA TÉCNICA---\n')
        print('La marca del coche es: ', self.marca) 
        print('El tipo del coche es:', self.tipo) 
        print('El modelo del coche es: ', self.modelo) 
        print('El color del coche es:', self.color)

#crearemos nuestro primer objeto de clase Vehiculo 
vehiculo=Vehiculo ('Toyota', 'Tacoma', '2024','Blanco') 
vehiculo.ficha_tecnica()