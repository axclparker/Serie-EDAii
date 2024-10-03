def llaveNum(llave):
    return llave % 7  

def insertarEnT(T, llave, metodo):
    j = 0
    m = len(T)
    h = llaveNum(llave)  
    while j < m:
        if metodo == 'lineal':
            i = (h + j) % m
        elif metodo == 'cuadratico':
            i = (h + j ** 2) % m
        elif metodo == 'doble':
            step = 1 + (llave % (m - 1))  
            i = (h + j * step) % m
        else:
            raise ValueError("Método no reconocido")

        if T[i] is None:
            T[i] = llave
            return i  
        j += 1  

    return False  

def buscar(T, llaveAlfa):
    j = 0
    m = len(T)
    x = llaveNum(llaveAlfa)
    h = x % m
    while j < m:
        indice = (h + j) % m
        print(f'Calculando índice: {indice}') 
        if T[indice] is None:
            return False 
        if T[indice] == llaveAlfa:
            return indice  
        j += 1
    return False 

def main():
    llaves = [2341, 4234, 2839, 430, 22, 397, 3920]
    
    print("Inserción con manejo de colisiones: Lineal")
    T_lineal = [None] * 7
    for llave in llaves:
        insertarEnT(T_lineal, llave, 'lineal')
    print("Tabla hash (Lineal):", T_lineal)

    print("\nInserción con manejo de colisiones: Cuadrático")
    T_cuadratico = [None] * 7
    for llave in llaves:
        insertarEnT(T_cuadratico, llave, 'cuadratico')
    print("Tabla hash (Cuadrático):", T_cuadratico)

    print("\nInserción con manejo de colisiones: Doble hashing")
    T_doble = [None] * 7
    for llave in llaves:
        insertarEnT(T_doble, llave, 'doble')
    print("Tabla hash (Doble hashing):", T_doble)

    llaves_a_buscar = [2839, 430]
    for llave in llaves_a_buscar:
        print(f'\nBuscando llave {llave} en tabla hash (Lineal):')
        resultado_lineal = buscar(T_lineal, llave)
        if resultado_lineal is not False:
            print(f'Llave {llave} encontrada en índice: {resultado_lineal}')
        else:
            print(f'Llave {llave} no encontrada')

        print(f'\nBuscando llave {llave} en tabla hash (Cuadrático):')
        resultado_cuadratico = buscar(T_cuadratico, llave)
        if resultado_cuadratico is not False:
            print(f'Llave {llave} encontrada en índice: {resultado_cuadratico}')
        else:
            print(f'Llave {llave} no encontrada')

        print(f'\nBuscando llave {llave} en tabla hash (Doble hashing):')
        resultado_doble = buscar(T_doble, llave)
        if resultado_doble is not False:
            print(f'Llave {llave} encontrada en índice: {resultado_doble}')
        else:
            print(f'Llave {llave} no encontrada')

main()
