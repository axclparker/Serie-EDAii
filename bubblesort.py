def bubbleSortSinMejora(A):
    n=len(A)
    cuenta = 0
    for i in range (1, n):
        for j in range (0,n - 1):
            if(A[j]>A[j + 1]):
                intercambia(A, j, j + 1)
                cuenta+=1

def bubbleSortMejorado(A):
    bandera = 1
    pasada = 0
    n = len(A)
    while pasada < (n - 1) and bandera == 1:
        bandera = 0
        for j in range(0, n-pasada-1):
            if A[j] > A[j+1]:
                bandera = 1
                intercambia2(A, j, j + 1)
        pasada += 1
               
def intercambia(A, j, i):
    tmp=A[j]
    A[j]=A[i]
    A[i]=tmp

def intercambia2(A, j, k):
    tmp = A[j]
    A[j] = A[k]
    A[k] = tmp

   
def principal():
    A=[5, 14, 6, 12, 7, 9, 2, 23, 11, 3]
    bubbleSortSinMejora(A)
    print(A)

    A=[5, 14, 6, 12, 7, 9, 2, 23, 11, 3]
    bubbleSortMejorado(A)
    print(A)

   
principal()
