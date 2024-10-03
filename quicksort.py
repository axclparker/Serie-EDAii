def intercambia(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def Particionar(A, p, r):
    x = A[r]  
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            intercambia(A, i, j)
    intercambia(A, i + 1, r)
    return i + 1

def QuickSort(A, p, r):
    if p < r:
        q = Particionar(A, p, r)
        print(f"\nProceso de ordenamiento de la lista: {A}")
        print(f"Numeros menores que el pivote ({A[q]}): {A[p:q]}")
        print(f"Numeros mayores que el pivote ({A[q]}): {A[q + 1:r + 1]}")
        QuickSort(A, p, q - 1)  
        QuickSort(A, q + 1, r) 

def principal():
    A = [5, 14, 6, 12, 7, 9, 2, 23, 11, 3]
    print("Original: ", A)
    QuickSort(A, 0, len(A) - 1)
    print("Final:  ", A)

principal()
