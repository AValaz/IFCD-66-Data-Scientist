## Ejercicio 101

import pandas as pd

datos_rendimiento = {
'nombre' : ['Pedro', 'Maria', 'Luis', 'Ana'],
'proyectos_completados' : [5,7,3,8],
'horas' : [40,35,50,30],
'satisfaccion' : [80,90,70,85]
}

df_rendimiento = pd.DataFrame(datos_rendimiento)
print(df_rendimiento)

df_rendimiento['metrica'] = 0.5*df_rendimiento['proyectos_completados']+0.3*df_rendimiento['horas']+0.2*df_rendimiento['satisfaccion']
print(df_rendimiento)