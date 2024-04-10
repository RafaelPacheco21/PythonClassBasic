#crearemos la super clase Animal con el encaberzado de una funcion 
#o método pero sin su cuerpo, similar a las interfaces de java
class Animal:
    def comunicarse(self):
        raise NotImplementedError('La subclase debe implementar el' 
                                  'cuerpo del método comunicarse()')

#crearemos las subclases que heredarán del método comunicarse pero 
#deben implementar el código de diferente forma según les convenga 
#es decir harán polimorfismo

class Perro (Animal):
    def comunicarse(self):
        return 'Soy un perro y ladro, Guuaauuu!!!'
    
class Gato (Animal):
    def comunicarse(self):
        return 'Soy un gato y maullo, Miiauuu!!!'

class Oso (Animal):
    def comunicarse(self):
        return 'Soy un oso y gruño, Ggrrrr!!!'
#como tenemos varios objetos, con métodos comunes, podemos meterlos en #una lista
animales=[Perro(), Gato(), Oso()]
#recorreremos la lista
for animal in animales:
    print(animal.comunicarse())