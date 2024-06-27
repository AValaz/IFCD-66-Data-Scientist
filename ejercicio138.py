## Ejercicio 138
## Ejercicio 137
import pandas as pd

dict = {'Alejandro': 8.5, 'Silvia': 4.9, 'Paula': 7.6, 'Javier':2.8, 'Victor':9.8}

def notas(dict):
    series = pd.Series(dict)
    series = series[series>5].sort_values(ascending=False)
    return series

print(notas(dict))