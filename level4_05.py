## Ejercicio 5
x = float(input("Cantidad a invertir en euros: "))
y = int(input("Número de años: "))
z = float(input("Interés anual: "))

i=0
while i<y:
    print(f"El capital obtenido es {round(x*((1+z)**y), 2)} euros")
    i+=1