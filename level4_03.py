## Ejercicio 3

def impares():
    numero = int(input("Dime un numero entero positivo: "))
    lista = ""
    for i in range(1, numero+1):
        if i%2!=0:
            lista +=f"{i},"
    return lista[0:len(lista)-1]    