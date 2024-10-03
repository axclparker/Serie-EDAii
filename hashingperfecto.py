def insertarPerfecto(T, llave):
    h = llave % len(T)  
    if T[h] is None: 
        T[h] = llave
    else:
        print(f'Colisión al insertar la llave {llave} en el índice {h}.')
        return False  
    return h  

def main():
    llaves = [2341, 4234, 2839, 430, 22, 397, 3920]
    T = [None] * 7 
    
    print("Inserción con hashing perfecto:")
    for llave in llaves:
        indice = insertarPerfecto(T, llave)
        if indice is not False:
            print(f'Llave {llave} insertada en índice {indice}')
        else:
            print(f'Llave {llave} no se pudo insertar debido a colisión.')

    print("\nTabla hash (Hashing Perfecto):", T)

main()
