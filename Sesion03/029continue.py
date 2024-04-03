#ejemplificaremos el uso de continue
#el programa imprimirá el valor de la variable unicamente cuando #esta sea impar
for i in range(1,11):
    if i%2==0:
        print('impresion normal omitida por ser numero par...')
        continue
    print('la variable i, vale:',i)