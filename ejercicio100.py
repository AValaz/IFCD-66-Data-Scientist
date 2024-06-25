## Ejercicio 100

import pandas as pd

datos_sensores = {
    'sensor_id' : [1,2,3,4,5],
    'temperatura' : [22,27,30,24,26],
    'humedad' : [55,65,60,58,63],
    'presion' : [1012,1008,1005,1011,1009]
}

df_sensores = pd.DataFrame(datos_sensores)
filtro = (df_sensores['temperatura']>25) & (df_sensores['presion']<1010)
df_filtrado =  df_sensores.loc[filtro, ['sensor_id', 'temperatura']]
print(df_filtrado)

