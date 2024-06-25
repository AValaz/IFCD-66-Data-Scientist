## Ejercicio 98

import pandas as pd
from functools import reduce


datos = {
    'nombre':['Carlos', 'Lucía', 'Marcos', 'Ana'],
    'matematicas': [90,85,78,92],
    'ciencias': [88,90,80,85],
    'inglés': [85,88,90,86]
}

df = pd.DataFrame(datos)
df_mod = df.copy()
df_mod['promedio'] = df_mod.mean(numeric_only=True, axis=1)
print(df_mod)