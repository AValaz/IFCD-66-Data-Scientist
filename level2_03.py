# Ejercicio 3

def funcion1 (func, lista):
    return [func(i) for i in lista]

def cuadrado (num):
    return num**2

ejemplo_lista = [5, 6, 30]
resultado = funcion1(cuadrado, ejemplo_lista)
print(resultado)

