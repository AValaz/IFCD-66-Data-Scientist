## Ejercicio 131

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\titanic.csv")
print(df.head())

# Diagrama de sectores con los fallecidos y supervivientes.
s = df['Survived'].value_counts()
print(s)
labels = ['Fallecidos', 'Supervivientes']
sizes = [s[0], s[1]]
fig, ax = plt.subplots(2,2)
ax[0,0].pie(sizes,labels = labels,  autopct='%1.1f%%')

# Histograma con las edades.
ax[0,1].hist(df['Age'], density=True)

# Diagrama de barras con el número de personas en cada clase.
clase = df.groupby(['Pclass'])['Pclass'].count()
ax[1,0].bar(clase.index, clase.values, color ='maroon',width = 0.4)
ax[1,0].set_title('Número de personas en cada clase')
ax[1,0].set_xlabel('Clase')
ax[1,0].set_ylabel('Número de personas')
ax[1,0].set_xticks(clase.index)
ax[1,0].set_xticklabels(clase.index)

# Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
clase_superv = df.groupby(['Pclass', 'Survived'])['Survived'].count().unstack()
ax[1,1].bar(clase_superv.index-0.2, clase_superv[0], width=0.4, label = 'Survived')
ax[1,1].bar(clase_superv.index+0.2, clase_superv[1], width=0.4, label = 'Not Survived')

plt.show()