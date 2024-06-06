# Ejercicio 9
x = float(input("Cantidad a invertir en euros: "))
y = float(input("Número de años: "))
z = float(input("Interés anual: "))

print(f"El capital obtenido es {round(x*((1+z)**y), 2)} euros")