## Variable objetivo. Modelo de clasificación binaria y binomial.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\heart.csv")

##  filtrado de columnas en un DataFrame de pandas, eliminando aquellas columnas que tienen un porcentaje de valores nulos superior a un umbral especificado. 
df_var = df.isnull().sum()
por = 10/100
df_var = df_var[df_var < por * len(df)]
list_var_OK = df_var.index
df = df[list_var_OK]

X, y = df.drop('target', axis=1).values, df['target'].values

# sns.countplot(x='target', data=df)
# plt.show()
# sns.heatmap(df.corr())
# plt.show()
# print(df.corr()['target'].sort_values())
# sns.scatterplot(x='target', y='cp', data = df)
# plt.hist2d(df['sex'], df['target'], bins=(2,2), cmap = plt.cm.viridis)
# plt.xlabel('sex')
# plt.ylabel('target')
# plt.colorbar()
# plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)
# print(X_train.shape)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

import os

# Suppress TensorFlow informational logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Disable oneDNN custom operations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout

model = Sequential()
num_neuronas = X_train.shape[1]
model.add(Dense(units = num_neuronas, activation='relu'))
model.add(Dense(units = num_neuronas/2, activation='relu'))
model.add(Dense(units = 1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')

model.fit(x=X_train, y=y_train, epochs = 300, validation_data = (X_test, y_test), verbose = 1)