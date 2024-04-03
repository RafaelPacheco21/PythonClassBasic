#Create (agregar) Read (leer o buscar) Update (actualizar) Delete (Eliminar) #Transaccionales (puntos de ventas) -->CRM-->ERP-->BSC
#Transaccionales(puntos de ventas)-->CRM-->ERP-->BSC 
#mysql
#create
import os #nos permite usar instrucciones de nuestro sistema operativo import time
import time
lista=[]
while True:
    print('---MENU PRINCIPAL---'
          '\n1. Insertar un dato.'
          '\n2. Eliminar un dato.'
          '\n3. Buscar un dato.'
          '\n4. Sobreescribir un dato.'
          '\n5. Mostrar el contenido de la lista.'
          '\n6. Salir.')
    opcion=int(input('Elige una opcion: '))
    if(opcion==1):#Create (Insertar)
        dato=input('Ingresa el dato a insertar: ')
        lista.append(dato)
        print('Dato insertado correctamente... ')
        time.sleep(2)
        os.system('cls')#limpia la pantalla linux o mac es clear
    elif (opcion==2): # Delete (Eliminar)
        dato=input('Ingresa el dato a Eliminar: ')
        if(dato in lista):
            lista.remove(dato)
            print('Dato eliminado correctamente... ')
            time.sleep(2)
            os.system('cls')
        else:
            print('El dato a eliminar no esta en la lista... ')
            time.sleep(2)
            os.system('cls')
    
    elif (opcion==3) : #read 
        dato=input('Ingresa el dato que buscaremos')
        if dato in lista:
            print('El dato existe en lista, está en la posición: ', lista. index(dato))
            time.sleep(2)
            os.system('cls')
        else:
            print('El dato no existe en la lista...')
            time.sleep(2)
            os.system('cls')
    elif(opcion==4):#update (sobreescribir)
        datoAnterior=input('Ingresa el dato a sobreescribir: ')
        if(datoAnterior in lista):
            indice=lista.index(datoAnterior)
            datoNuevo =input('Ingresa el dato nuevo: ')
            lista[indice]=datoNuevo
            print('El dato se sobreescribio correctamente...')
            time.sleep(2)
            os.system('cls')
        else:
            print(f'El dato {datoAnterior} no existe en la lista...') 
            time.sleep(2)
    elif(opcion==5):#Mostrar el contenido de la lista.\
        print('El contenido de la Lista es: ')
        print(lista)
        time.sleep(4)
        os.system('cls')
    elif(opcion==6):#Salir.
        respuesta=input('Estas seguro que quieres salir? (s/n): ')
        if(respuesta=='s' or respuesta=='S'):
            print('Saliendo...')
            time.sleep(2)
            os.system('cls')
            break
        time.sleep(2)
        os.system('cls')
    else:
        print('Opción no valida...')