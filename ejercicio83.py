## Ejercicio 83

list_tuplas = [(i, j) for i in range(1, 101) for j in range(1, 101) if i<j and (i*j)%7==0]

print(list_tuplas)