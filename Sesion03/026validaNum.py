#este programa valida para que solo se introduzca datos numericos
while True:
    try:
        datos=input('Por favor ingresa tue dad: ')
        edad=int(datos) #operacion de riesgo que ocupa un try --except
        if (edad<0) or (edad>=100):
            print('Edad no valida')
        else:
            break #Se sale porque si encontro un numero mayor que 0
    except ValueError: #si ocurre una excepcion
        print('Error al capturar, por favor, ingresa un dato numerico. ')

print('Edad valida: ',edad)