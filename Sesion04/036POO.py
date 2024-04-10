#crearemos la clase Persona 
#myself yourself
class Persona:
    #esta es la parte privada del objeto
    def __init__(self, nombre, edad) : #después de self van los atributos  
        self.nombre=nombre
        self.edad=edad
    
    def saludar(self): #parte pública del objeto
        print(f'Hola, mi nombre es: {self.nombre} y mi edad: {self.edad}')

#crearemos los objetos de la clase Persona
persona1=Persona ('Juan',25)
persona2=Persona ('Ana', 31)
print('Se construyeron 2 objetos, personal y persona2\n') 
#accederemos a los atributos de estos objetos
print('El nombre de la persona 1 es: ', persona1.nombre) 
print('La edad de la persona 1 es: ', persona1.edad)
print(f'\nEl nombre de la persona 2 es: , {persona2.nombre}'
      f' la edad de la persona 2 es: , {persona2.nombre}')
#accederemos a los metedos de los objetos
persona1.saludar()
persona2.saludar()