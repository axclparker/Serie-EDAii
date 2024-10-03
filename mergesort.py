def MergeSort(A, p, r):
    if p < r:
        q = int((p + r)/2)
       
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Mezcla(A, q, p, r)
       
def Mezcla(A, q, p, r):
    izq = A[p:(q + 1)]
    der = A[q + 1 : r + 1]
   
    i = j = 0
    for k in range(p, r + 1):
        if(j >= len(der)) or (i < len(izq) and izq[i] < der[j]):
            A[k] = izq[i]
            i += 1
        else:
            A[k] = der[j]
            j += 1
   
def principal():
  A=[5, 14, 6, 12, 7, 9, 2, 23, 11, 3]
  MergeSort(A, 0, len(A) - 1)
  print(A)

   
principal()
