#Pediremos una cantidad en pesos y mostraremos un menu de opciones
#para convertir en Dolares y en Soles Peruanos
pesos=int(input('Escribe la cantidad en Pesos Mexicanos: '))
opcion=int(input('\nA cual moneda los quieres convertir:'
                 '\n1. Dolares $17'
                 '\n2. Soles Peruanos $4 \n'))
#apoyado por Jorge Beristain
mensaje='La cantidad convertida en Dolares es:'
ancho=50
nuevomensaje=mensaje.center(ancho)
if(opcion==1):                           
    total=pesos/17
    print(nuevomensaje,round(total,2))
elif(opcion==2):
    total=pesos/4
    print('La cantidad convertida en Soles Peruanos es:',round(total,2))
else:
    print('Elegiste una opción no válida...')