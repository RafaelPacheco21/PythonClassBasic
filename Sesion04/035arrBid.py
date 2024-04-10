#crearemos una lista de listas que llenaremos desde el teclado 
filas=5
columnas=5
matriz=[[1]*columnas for _ in range(filas)]
#File Allocation Table (tabla de localizacion de archivos) FAT
for i in range(filas):
    for j in range(columnas):
        dato=input('Ingresa el dato para la posición: ({},{})'.format(i,j)) 
        matriz[i][j]=dato

print('\n Los datos de la matriz son: ')
for fila in matriz:
    print(fila)

#imprimiremos la diagonal principal de la matriz
print('\nimprimiremos la diagonal principal de la matriz')
for i in range(5):
    for j in range(5): 
        if i==j:
            print(matriz[i][j])
print('\nimprimiremos la diagonal principal en orden inverso')
for i in range(4,-1,-1):
    for j in range(4,-1,-1): 
        if i==j:
            print(matriz[i][j])