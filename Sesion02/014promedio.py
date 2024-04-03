#El programa evaluara la estatura del usuario y
#si la estatura es menor a 160 cm imprimira: eres chato
#si la estatura esta entre 160 y 175 cms imprimira: eres de 
#estatura mediana
#si la estatura es mayor a 175 cm imprimira: eres alto

nombre=input('Escribe tu nombre: ')
estatura=int(input('Escribe tu estatura en centimetros(cm): '))

if(estatura<160):
    print(f' {nombre} eres chato...')

if(estatura>=160) and (estatura<=175):
    print(f' {nombre} eres de estatura mediana...')

if(estatura<175):
    print(f' {nombre} eres alto...')