## Ejercicio 99
import pandas as pd

datos_ventas = {
        'producto':['A','B','A','C','B','A','C'],
        'cantidad':[10,5,20,15,10,5,10],
        'precio':[100,200,100,150,200,100,150]
}

df_ventas = pd.DataFrame(datos_ventas)

df_grouped = df_ventas.groupby(by = ['producto', 'precio']).sum().reset_index()
df_grouped ['ingreso total'] = df_grouped['precio']*df_grouped['cantidad']
print(df_grouped)

