def radixSort(A):
    max1 = max(A)  

    exp = 1
    while max1 // exp > 0:  
        countingSortForRadix(A, exp)
        exp *= 10  
def countingSortForRadix(A, exp):
    n = len(A)
    B = [0] * n  
    C = [0] * 10  

    for i in range(n):
        index = (A[i] // exp) % 10
        C[index] += 1 

    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        index = (A[i] // exp) % 10
        B[C[index] - 1] = A[i]
        C[index] -= 1

    for i in range(n):
        A[i] = B[i]

A = [345, 876, 324, 245, 514, 531, 841]
radixSort(A)
print("Arreglo ordenado:", A)
