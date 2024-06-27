## Ejercicio 137
import pandas as pd

dict = {'Alejandro': 8.5, 'Silvia': 5.7, 'Paula': 7.6}

def notas(dict):
    series = pd.Series(dict)
    index = ['Mínima', 'Máxima', 'Media', 'Desviación']
    valores = [series.min(),series.max(),series.mean(), series.std()]
    pandas = pd.Series(valores, index=index)
    return pandas

print(notas(dict))