## Ejercicio 140
import pandas as pd

dict = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
        'Ventas': [30500,35600,28300,33900],
        'Gastos': [22000,23400,18100,20700]}

df = pd.DataFrame(dict)

def balance(df, meses):
    df = df[df['Mes'].isin(meses)]
    df['Balance'] = df['Ventas']-df['Gastos']
    return df

mes = ['Enero']
print(balance(df, mes))