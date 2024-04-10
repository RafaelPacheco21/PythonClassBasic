import pooLib041

class UsuariosPremium (pooLib041.Usuario):
    def __init__(self, id, alias, nombre, apellidos, sorteos, puntos): 
        super().__init__(id, alias, nombre, apellidos)
        self.sorteos=sorteos
        self.puntos=puntos
    
    def muestra_datos (self):
        super(). muestra_datos()
        print(f'Tienes derecho a participar en {self.sorteos} sorteos') 
        print(f'Tienes {self.puntos} puntos para canjear en premios')

#crearemos un objeto de la clase Usuarios Premium id=input('Introduce el id del usuario: ')
alias=input('Escribe el alias del usuario: ')
nombre=input('Escribe el nombre del usuario: ')
apellidos=input('Escribe los apellidos del usuario: ')
sorteos=25
puntos=500
userPremium=UsuariosPremium(id, alias, nombre, apellidos, sorteos, puntos) 
userPremium.muestra_datos()