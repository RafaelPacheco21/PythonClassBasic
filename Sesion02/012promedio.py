#el programa calcula y muestra el promedio de 3 calificaciones

print ("El programa calcula el promedio de 3 calif. de una alumno\n")

nombre=input('Escribe tu nombre Alumno: ')
mat=float(input('Escribe tu calif. de Matemáticas: '))
fis=float(input('Escribe tu calif. de Física: '))
quim=float(input('Escribe tu calif. de Química: '))

#procesamiento de datos
promedio=(mat+fis+quim)/3
'''pioridad de operadores aritméticos
exponenciación ** y los paréntesis () en primer lugar
* y /                                 en segundo lugar
+ y -                                 en tercer lugar
'''
# mat + fis + quim/3 no es lo mismo que promedio=(mat+fis+quim)/3
# Salida de datos
print(nombre, 'Tu promedio es: ', round(promedio,2)) #round es para indicar 2 decimales
#Además el programa debe avisar si está aprobado o no el alumno
if (promedio<6):#esta es la forma básica de la estructura selectiva if
    print(nombre, 'Lo sentimos estás reprobado')
    #hasta aquí es la forma básica de la estructura selectiva if
else:
    print(nombre, 'Felicitaciones, estás aprobado...')
    #hasta aquí es la estructura selectiva if completa