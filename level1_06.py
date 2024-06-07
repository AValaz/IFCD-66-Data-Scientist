# Ejercicio 6
x = int(input("Dime un numero entero positivo "))

## Añadimos la comprobación

if x<0: # permite modificar la conducta del usuario ante la entrada de un negativo
    condicion = True  # variable centinela que permite al codigo salir de la espiral de pedir el entero positivo
    while condicion: #bucle para comprobar que sea positivo
        print("El número introducido es negativo.") #advertencia
        x = int(float(input("Introduce un entero positivo: "))) #introducir de nuevo el numero
        if x>0: #comprobación en bucle de positividad
            condicion = False # cambio para salir del bucle
        else:
                pass # cumplir con pep
else:
    pass # cumplir con pep

suma = int(x*(x+1)/2)
print(suma)