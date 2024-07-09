import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn.cluster import KMeans
from statsmodels.stats.proportion import proportions_ztest
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, Binarizer, PowerTransformer

df = pd.read_csv("C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\diabetes.csv") # names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'])

X, Y = df.values[:,0:8], df.values[:, 8]

scaler_minMax = MinMaxScaler(feature_range=(0,1))
rescaledX_minMax = scaler_minMax.fit_transform(X)
np.set_printoptions(precision=3)
rescaledX_minMax
df_transform = pd.DataFrame(data = np.column_stack((np.asarray(rescaledX_minMax), np.asarray(Y))), columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'])

scaler_standar = StandardScaler()
rescaledX_standar = scaler_standar.fit_transform(X)
df_transform_standar = pd.DataFrame(data = np.column_stack((np.asarray(rescaledX_standar), np.asarray(Y))), columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'])

scaler_normal = Normalizer()
rescaledX_normal = scaler_normal.fit_transform(X)
df_transform_normal = pd.DataFrame(data = rescaledX_normal, columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age'])

scaler_binarizado = Binarizer(threshold=0.0)
rescaledX_binarizado = scaler_binarizado.fit_transform(X)
df_transform_binarizado = pd.DataFrame(data = rescaledX_binarizado, columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age'])
print(df_transform_binarizado)

features = df[['DiabetesPedigreeFunction', 'Age']]
scaler_YeoJohnson = PowerTransformer(method='yeo-johnson', standardize=True)
feature_YeoJohnson = scaler_YeoJohnson.fit(features)
cal_lambas_yo = feature_YeoJohnson.lambdas_
feature_YeoJohnson = scaler_YeoJohnson.transform(features)
df_features_YeoJohnson = pd.DataFrame(data = feature_YeoJohnson, columns=['DiabetesPedigreeFunction', 'Age'])
print(df_features_YeoJohnson)