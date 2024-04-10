#crearemos una clase y un objeto normales
class Usuario:
    def __init__(self,id, alias, nombre, apellidos):
        self.id=id
        self.alias=alias
        self.nombre=nombre
        self.apellidos=apellidos
    
    def muestra_datos (self):
        print('El id del usuario es:', self.id)
        print('El alias del usuario es:', self.alias)
        print('El nombre del usuario es: ', self.nombre)
        print('Los apellidos del usuario son:', self.apellidos) 
#crearemos el objeto de esta clase y usaremos su métodos 
#user=Usuario(13, 'Fer', 'Jesus Fernando', 'Cruz Álvarez') 
#user.muestra_datos()