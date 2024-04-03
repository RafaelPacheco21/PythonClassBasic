#Simularemos el conteo regresivo del despeque de un cohete
import time

contador=10
print('Inicia el conteo regresivo . . .')
while contador>0: #puede que el ciclo nunca se ejecute
    print(contador)
    time.sleep(1)
    contador-=1 #contador-1
print('El cohete ha despegado despegado con exito...')