## ejercicio 7

def tablas():
    numero = int(input("Dime un número y te diré la tabla de multiplicar: "))
    for i in range(1, 11):
        print(f"{i}*{numero} es igual a {i*numero}")
    
print(tablas())

