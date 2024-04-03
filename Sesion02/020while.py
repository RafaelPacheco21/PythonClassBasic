#El programa contiene un numero secreto que el usaurio debe adivinar
#tendrá 3 oportunidades

numero_secreto=9
adivinado=False
intentos=0
quedan=3

print('Solo tienes 3 intentos')
while not(adivinado)and(intentos<3):# while (adivinado==False)
    dato=int(input('Adivina el numero (Es menor que 10): '))
    if(dato==numero_secreto):
        print('Felicitaciones, has adivinado el número...')
        adivinado=True
    else:#si no lo adivinó
        intentos+=1
        if(intentos==3):#si intentos ya llegó a 3
            print('Juego terminado...')
        else:#en caso que todavia no sea igual a 3
            print('Por favor intentalo de nuevo...')
            quedan-=1
            print(f'Te quedan {quedan} intentos')