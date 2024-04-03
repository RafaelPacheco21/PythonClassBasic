#El usuario indicara un numero de dia y se le imprimira el nombre de 
#ese dia
nombre=input('Escribe tu nombre: ')
dia=int(input('Escribe el numero de dia que quieres venir a trabajar: '))

if(dia==1):
    print(f'{nombre} felicidades vendras a trabajar el dia lunes. ')
elif (dia==2):
    print(f'{nombre} felicidades vendras a trabajar el dia martes. ')
elif (dia==3):
    print(f'{nombre} felicidades vendras a trabajar el dia miercoles. ')
elif (dia==4):
    print(f'{nombre} felicidades vendras a trabajar el dia jueves. ')
elif (dia==5):
    print(f'{nombre} felicidades vendras a trabajar el dia viernes. ')
elif (dia==6):
    print(f'{nombre} felicidades vendras a trabajar el dia sabado. ')
elif (dia==7):
    print(f'{nombre} felicidades vendras a trabajar el dia domingo. ')
else:
    print(f'{nombre}, lo sentimos ese dia no es valido...')