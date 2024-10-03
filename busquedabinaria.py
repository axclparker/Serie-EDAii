import random 

def busquedaBinaria(A, x, p, q):
  while p <= q:
    medio = ((p + q) // 2)
    if x == A[medio]:
      return medio
    else:
      if A[medio] > x:
        q = medio - 1
      else:
        p = medio + 1
  return -1

def main():
    A = [3, 5, 6, 18, 11, 12, 14, 15, 17, 18]
    x = 13
    y = 18
    z = 3
    q = len(A) - 1

    index1 = busquedaBinaria(A, x, 0, q)
    if index1 != -1:
        print(f'El elemento {x} fue encontrado en el índice: {index1}')
    else:
        print(f'El elemento {x} no fue encontrado')

    index2 = busquedaBinaria(A, y, 0, q)
    if index2 != -1:
        print(f'El elemento {y} fue encontrado en el índice: {index2}')
    else:
        print(f'El elemento {y} no fue encontrado')

    index3 = busquedaBinaria(A, z, 0, q)
    if index3 != -1:
        print(f'El elemento {z} fue encontrado en el índice: {index3}')
    else:
        print(f'El elemento {z} no fue encontrado')

main()