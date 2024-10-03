def heapify(A, n, i):
    largest = i 
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  
        heapify(A, n, largest)  

def heapSort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  
        heapify(A, i, 0)  
   
def principal():
    A=[5, 14, 6, 12, 7, 9, 2, 23, 11, 3]
    heapSort(A)
    print(A)

   
principal()
