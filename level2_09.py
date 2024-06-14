## Ejercicio 9
def vector (*numbers):
    suma = 0
    for num in numbers:
        suma+=num**2
    suma = suma**(1/2)

    return suma
print(vector(2,2,3,4))

## Solución profesor 
# from functools import reduce

# def cuadrado(i,j):
#     return i+j**2

# def modulov1(v):
#     l = [x**2 for x in v]
#     c = 0 
#     for k in l:
#         c+=k
#     return c

# def modulo_v2(v):
#     return reduce(cuadrado, v, 0) ** 0.5

# print(modulo((2,2,3)))


