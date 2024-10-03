import random

def CountingSort(A, k):
    C = [0 for i in range(k + 1)]

    for j in range(len(A)):
        C[A[j]] += 1
    
    print("Conteo de ocurrencias:")
    for i in range(len(C)):
        print(f'{i} - {C[i]}')

    for i in range(1, k + 1):
        C[i] += C[i - 1]
    
    print("\nPosiciones acumuladas:")
    for i in range(len(C)):
        print(f'{i} - {C[i]}')

    B = [0 for i in range(len(A))]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B

k = 12
A = [6, 2, 4, 7, 1, 0, 2, 8, 3, 8, 9, 3, 5]

B = CountingSort(A, k)
print("\nArreglo ordenado de menor a mayor:")
print(B)
