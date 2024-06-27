## ejercicio 142
import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\titanic.csv")

## Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, 
# los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas

# print(f"Tamaño: {df.size}")
# print(f"Forma: {df.shape}")
# print(f"Nombre columnas: {df.columns}")
# print(f"10 primeras filas:\n {df.head()}")
# print(f"10 últimas filas:\n {df.tail()}")

# Mostrar por pantalla los datos del pasajero con identificador 148.
# print(df[df['PassengerId']==148])

# Mostrar por pantalla las filas pares del DataFrame.
# print(df.iloc[::2])

#Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
# print(df[df['Pclass'] == 1][['Name', 'Pclass']])
# primera_clase = df[df['Pclass'] == 1][['Name', 'Pclass']].sort_values(by = ['Name'])
# print(first_class_names)

# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
# perc_superv = df['Survived'].sum()/df['Survived'].count()*100
# print(f'El porcenatje de personas que sobreviveron es {perc_superv:.2f}% y de los que no {100-perc_superv:.2f}%')

# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
# superv_clase = superv_clase = df.groupby(['Pclass', 'Survived']).agg({'PassengerId':'count'})
#df.groupby(['Pclass', 'Survived']).count()['PassengerId']
# porc_superv_clase = superv_clase.apply(lambda x: 100*x/float(x.sum()))
# print(porc_superv_clase)

# Eliminar del DataFrame los pasajeros con edad desconocida.
# print(df[df['PassengerId']==6])
df = df[df['Age'].notna()]

# Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
# print(df[df['Sex']== 'female'].groupby('Pclass')['Age'].mean())

# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df['Menor'] = np.where(df['Age']<18, True, False)
# print(df[['Age', 'Menor']].head(10))

# 11.Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
grouped = df.groupby(['Menor', 'Pclass']).agg({'Survived': ['sum', 'count']})
grouped.columns = ['Survived', 'Total']
grouped['Survival Rate (%)'] = (grouped['Survived'] / grouped['Total']) * 100
print(grouped)
