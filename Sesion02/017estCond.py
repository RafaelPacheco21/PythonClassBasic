#Convertiremos de metros a kilómetros y a centímetros según lo solicite el usuario

distancia=float(input('Escribe la cantidad en metros: '))
opcion=input('\n A que unidad quieres convertir?'
             '\n a. Convertir a Kilómetros'
             '\n b. Convertir a Centímetros\n')
if opcion=='a':
    total=distancia/1000
    print('La cantidad convertida en kilómetros es: ', total)
elif opcion=='b':
    total=distancia*100
    print('La cantidad convertida en centímetros es: ', total)
else:
    print('Opción no válida...')