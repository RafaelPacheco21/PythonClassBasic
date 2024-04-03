


matriz= [ [1,2,3],[4,5,6], [7,8,9]]

elemento=matriz[1][2]
print('El dato que esta en la fila 1, columna 2 es: ', elemento)

print('\n Ahora recorremos toda la estructura:')
for fila in matriz:
    for elemento in fila:
        print(elemento, end='')
        print()


