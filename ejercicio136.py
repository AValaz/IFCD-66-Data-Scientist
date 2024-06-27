## Ejercicio 136
import pandas as pd

years = [2020, 2022, 2023]
i=0
ventas =[]
while i<len(years):
    x = float(input(f"Dime las ventas del año {years[i]}: "))
    i+=1
    ventas.append(x)


serie_ventas = pd.Series(ventas, index=years)

print(f"La ventas han sido\n{serie_ventas}")
print(f"La ventas con un descuento han sido\n{serie_ventas*0.9}")