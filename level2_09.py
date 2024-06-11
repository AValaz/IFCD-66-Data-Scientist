## Ejercicio 9
def vector (*numbers):
    suma = 0
    for num in numbers:
        suma+=num**2
    suma = suma**(1/2)

    return suma
print(vector(2,2,3,4))