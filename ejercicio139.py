## Ejercicio 139
import pandas as pd

dict = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
        'Ventas': [30500,35600,28300,33900],
        'Gastos': [22000,23400,18100,20700]}

df = pd.DataFrame(dict)
print(df)