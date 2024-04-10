#mostraremos como se comporta la herencia en python
#primero crearemos la super clase, clase base o clase padre 
class Animal:
    def __init__(self, nombre):
        self.nombre=nombre
    
    def comer (self):
        print (f'{self.nombre} está comiendo')

#crearemos la sub clase, clase derivada o clase hija 
class Perro (Animal): #hay herencia de la super clase Animal 
    def __init__(self, nombre, raza):
        super().__init__(nombre) #atributo heredado de la superclase
        self.raza=raza #atributo propio de la clase Perro
    
    def ladrar (self):
        print(f'{self.nombre} es de la raza {self.raza} y está ladrando')

#crearemos el objeto de la clase Perro
print('Crearemos el objeto miPerro, de clase Perro\n'
      'que hereda atributos de la super clase Animal\n' 
      'Su nombre será Simba y su raza Labrador\n') 
miPerro=Perro ('Simba', 'Labrador')
miPerro.comer() #este método es de la super clase 
miPerro.ladrar() # este método es de la sub clase