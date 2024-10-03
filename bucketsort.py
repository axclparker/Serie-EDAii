def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucketSort(A):
    n = len(A)  
    
    B = [[] for _ in range(n)]
    
    for i in range(n):
        index = int(n * A[i])  
        B[index].append(A[i])  
    
    for i in range(n):
        insertionSort(B[i])
    
    sorted_array = []
    for i in range(n):
        sorted_array.extend(B[i])  
    
    return sorted_array

A = [.223, .45, .567, .225, .0123, .876, .093, .9, .6, .94, .93, .76, .73, .23]

sorted_A = bucketSort(A)
print("Arreglo ordenado:", sorted_A)
