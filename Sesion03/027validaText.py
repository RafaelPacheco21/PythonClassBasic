#el programa valida entradas de tipo texto
while True:
    try:
        dato=input('Ingresa tu nombre de usuario: ') 
        nombre=int(dato) #operacion riesgosa
        print('Error, por favor ingresa solo texto, no números.') 
    except ValueError:
        break

print('Nombre valido: ', dato)