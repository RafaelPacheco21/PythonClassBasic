
def es_par(num):
    if num%2==0:
        return True
    else:
        return False

numero=int(input('Escribe un número y determinaré si es par o impar: '))

if es_par(numero):
    print(f'el número {numero} es par')
else:
    print(f'El número {numero} es impar')
