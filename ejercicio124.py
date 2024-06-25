## Ejercicio 124
import numpy as np
import matplotlib.pyplot as plt

años = [2015, 2016, 2017, 2018]
i=2015
lista_ventas = []

while i<=2018:
    ventas = float(input(f'Dime las ventas dedl año {i}: '))
    lista_ventas.append(ventas)
    i+=1

fig, ax = plt.subplots()
ax.plot(años, lista_ventas, color = "r")
plt.show()

