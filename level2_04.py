# Ejercicio 4

def funcion1 (func, lista):
    return [func(i) for i in lista]

def booleana (num):
    if num>=0:
        return True
    else: 
        return False

lista_ejemplo = [-1, 1, 5, 0]

resultado = funcion1(booleana, lista_ejemplo)
print(resultado)