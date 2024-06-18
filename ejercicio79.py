## Ejercicio 79
import csv

try:
    with open("salidas//cartera-acciones.csv") as f:
        filas = csv.reader(f)
        sum=sum(float(row[1])*float(row[2]) for row in filas)
except FileNotFoundError:
    print("Archivo no encontrado")

print(sum)