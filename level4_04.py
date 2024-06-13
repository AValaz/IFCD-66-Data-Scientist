## Ejercicio 4

def cuenta_atras():
    numero = int(input("Dime un numero entero positivo: "))
    lista = ""
    for i in range(numero, -1, -1):
        lista +=f"{i},"
    return lista[0:len(lista)-1]    

print(cuenta_atras())