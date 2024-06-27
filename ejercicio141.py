## Ejercicio 141
import pandas as pd


# def cotizacion(r):
#     df = pd.read_csv(r, sep=';')




ruta = "C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\cotizacion.csv"
df = pd.read_csv(ruta, sep=';')
df['Final'] = df['Final'].str.replace('.', '').str.replace(',', '.')
df['Máximo'] = df['Máximo'].str.replace('.', '').str.replace(',', '.')
df['Mínimo'] = df['Mínimo'].str.replace('.', '').str.replace(',', '.')
df['Volumen'] = df['Volumen'].str.replace('.', '').str.replace(',', '.')
df['Efectivo'] = df['Efectivo'].str.replace('.', '').str.replace(',', '.')

df[['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']] = df[['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']].apply(pd.to_numeric)

valor_max = df[['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']].max(axis=0)
valor_min = df[['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']].min(axis=0)
valor_medio = df[['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']].mean(axis=0, numeric_only=True)

df_valores = pd.DataFrame({
    'Maximo' : valor_max,
    'Mínimo' : valor_min,
    'Media': valor_medio
})

print(df_valores)