## Ejercicio 81
palabras = ['hola', 'adios', 'perro', 'kjhnmj', 'alejandría']
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
dict = {i:i[::-1] for i in palabras if len(i)>5 and not any(v in i for v in vocales)}

print(dict)