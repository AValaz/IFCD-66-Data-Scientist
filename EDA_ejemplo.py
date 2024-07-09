import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn.cluster import KMeans
from statsmodels.stats.proportion import proportions_ztest

df = pd.read_csv("C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\titanic.csv")

# print(df.columns)
# print(df.shape)
# print(df.dtypes)
# print(df.select_dtypes(include = ['object']).shape[1])

# print(round(df['Survived'].value_counts(normalize=True)[0],4)*100)

# sns.countplot(x = 'Survived', data = df)
# plt.title('Proporción de fallecidos y supervivientes')
# plt.xlabel('0=Muerto 1=Superviviente')
# plt.ylabel('Num. Personas')
# plt.xticks([0,1], ['Muerto', 'Superviviente'])
# plt.show()

#Contraste de hipótesis: binomial
# proporcion_supervivientes = df['Survived'].mean()
# n_total = df['Survived'].shape[0]
# n_supervivientes = df['Survived'].sum()
# print(stats.binomtest(n_supervivientes, n_total, proporcion_supervivientes, alternative = 'two-sided').pvalue) #p-value = 1. Por tanto, aceptamos la hipótesis nula de que si que es una binomial

# print(df['Age'].value_counts(dropna=False))
# print(df['Age'].isnull().sum()/df['Age'].count()*100)
# print(df['Age'].isnull().sum()/df['Age'].shape[0]*100)
# print(df['Age'].isnull().sum())
# print(df['Age'].max())
# print(df['Age'].min())

#Tipo de kurtosis
# print(df['Age'].kurtosis())
# print(df['Age'].skew()) #Vemos hacia donde se desplaza la media

# plt.subplot(1,2,1)
# sns.boxplot(x='Age', data = df)
# plt.title("Día caja y bigotes de Age")
# plt.xlabel('Edad en años')

# plt.subplot(1,2,2)
# sns.histplot(x=df['Age'], bins = 30, kde = True)
# plt.title("Histograma con KDE de Age")
# plt.xlabel('Edad en años')
# plt.ylabel("Frecuencia")

# plt.tight_layout()
# plt.show()

# Valores que faltan
# IQR = df['Age'].quantile(0.75)-df['Age'].quantile(0.25)

# LS = df['Age'].quantile(0.75)+1.5*IQR
# LI = df['Age'].quantile(0.25)-1.5*IQR

# # ¿Cuántas personas son? ID y nombre de esas personas. Outliers a la derecha
# print(df[df['Age']>LS][['PassengerId','Name', 'Age']])
# out = df[df['Age']>LS][['PassengerId','Name', 'Age']]

# plt.scatter(out.index, out['Age'], color='red', label = 'outlier')
# plt.legend()
# plt.show()

## Contraste de hipótesis
# stats, p = stats.shapiro(df['Age'].dropna())

# plt.figure(figsize=(4,4))
# stats.probplot(df['Age'].dropna(), dist = 'norm', plot = plt)
# plt.show()

## Clusterización
# kmeans = KMeans(n_clusters = 2, random_state=0).fit(df['Age'].dropna().values.reshape(-1,1))
# labels = kmeans.labels_
# df['AgeCluster'] = pd.Series([np.nan]*len(df))
# df.loc[~df['Age'].isnull(),'AgeCluster'] = labels

# grupo1 = df.loc[df['AgeCluster']==0, 'Age'].dropna()
# grupo2 = df.loc[df['AgeCluster']==1, 'Age'].dropna()
# print(f"G1: x:{grupo1.mean():.2f} - me:{grupo1.median():.2f} - std:{grupo1.std():.2f}")
# print(f"G1: x:{grupo2.mean():.2f} - me:{grupo2.median():.2f} - std:{grupo2.std():.2f}")

# df_c = df.dropna(subset = ['Age']).copy()
# df_c['AgeCluster'] = kmeans.labels_

# plt.figure(figsize=(15,5))

# plt.subplot(1,2,1)
# sns.boxplot(x='AgeCluster', y = 'Age', data = df_c)
# plt.title("Edad por cluster")
# plt.xlabel('Cluster de edad')
# plt.xlabel('Edad en años')

# plt.subplot(1,2,2)
# sns.histplot(data = df_c, x = 'Age', hue = 'AgeCluster', kde=True, bins = 20)
# plt.title("Histograma de clusters")
# plt.xlabel('Edad en años')
# plt.xlabel('Frecuencia')

# plt.show()


## Test de proporciones
# tasa_superviviencia = df.groupby('AgeCluster')['Survived'].mean()
# n1 = len(df[df['AgeCluster']==0])
# n2 = df[df['AgeCluster']==0].shape[0]
# s1 = df[df['AgeCluster']==0]['Survived'].sum()
# s2 = df[df['AgeCluster']==1]['Survived'].sum()

# c = np.array([s1,s2])
# n = np.array([n1, n2])

# z_stat, p_value = proportions_ztest(c, n)
# print(z_stat)
# print(p_value) ##Rechazamos H0, no hay evidencia para afirmar que la tasa de superviviencia de ambas poblaciones es diferente.

## Variable sexo

## Sexo determina la supervivencia?
#print(df['Sex'].value_counts(normalize=True).iloc[0])
# sns.countplot(data=df, x ='Sex')
# plt.show()

# Tablas de contigencia
print(pd.crosstab(df['Sex'], df['Survived'], margins=True, normalize='index').round(4)*100)