def busquedaLineal(A, n, x):
    encontrado = -1
    comparaciones = 0  
    for k in range(0, n):
        comparaciones += 1
        if x == A[k]:
            encontrado = k
            break
    return encontrado, comparaciones

def sinMejora():
    A = [3, 5, 6, 18, 11, 12, 14, 15, 17, 18]
    x = 13
    y = 18
    z = 3

    index1, comparaciones1 = busquedaLineal(A, len(A), x)
    if index1 != -1:
        print(f'El elemento {x} fue encontrado en el índice: {index1} después de {comparaciones1} comparaciones.')
    else:
        print(f'El elemento {x} no fue encontrado después de {comparaciones1} comparaciones.')

    index2, comparaciones2 = busquedaLineal(A, len(A), y)
    if index2 != -1:
        print(f'El elemento {y} fue encontrado en el índice: {index2} después de {comparaciones2} comparaciones.')
    else:
        print(f'El elemento {y} no fue encontrado después de {comparaciones2} comparaciones.')

    index3, comparaciones3 = busquedaLineal(A, len(A), z)
    if index3 != -1:
        print(f'El elemento {z} fue encontrado en el índice: {index3} después de {comparaciones3} comparaciones.')
    else:
        print(f'El elemento {z} no fue encontrado después de {comparaciones3} comparaciones.')

sinMejora()

def busquedaLinealMejorado(A, n, x):
    encontrado = -1
    comparaciones = 0  
    for k in range(n - 1):
        comparaciones += 1
        if A[k] == x:
            encontrado = k
            break
    return encontrado, comparaciones

def conMejora():
    A = [3, 5, 6, 18, 11, 12, 14, 15, 17, 18]
    x = 13
    y = 18
    z = 3

    index1, comparaciones1 = busquedaLinealMejorado(A, len(A), x)
    if index1 != -1:
        print(f'El elemento {x} fue encontrado en el índice: {index1} después de {comparaciones1} comparaciones.')
    else:
        print(f'El elemento {x} no fue encontrado después de {comparaciones1} comparaciones.')

    index2, comparaciones2 = busquedaLinealMejorado(A, len(A), y)
    if index2 != -1:
        print(f'El elemento {y} fue encontrado en el índice: {index2} después de {comparaciones2} comparaciones.')
    else:
        print(f'El elemento {y} no fue encontrado después de {comparaciones2} comparaciones.')

    index3, comparaciones3 = busquedaLinealMejorado(A, len(A), z)
    if index3 != -1:
        print(f'El elemento {z} fue encontrado en el índice: {index3} después de {comparaciones3} comparaciones.')
    else:
        print(f'El elemento {z} no fue encontrado después de {comparaciones3} comparaciones.')

conMejora()
