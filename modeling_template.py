# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Paso 1: Cargar los datos
# Aquí se asume que tienes un archivo CSV. Ajusta según sea necesario.
df = pd.read_csv('ruta_al_archivo.csv')

# Paso 2: Exploración y limpieza de datos
# Verificar los datos
print(df.head())
print(df.info())
print(df.describe())

# Eliminar filas con valores nulos en una columna específica (ajusta según tus datos)
df = df.dropna(subset=['column_name'])

# Eliminar filas con valores específicos
df = df[df['Home_Owner'] != 'Other']

# Paso 3: Preprocesamiento de datos
# Separar características (X) y objetivo (y)
X = df.drop('target', axis=1).values
y = df['target'].values

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)

# Escalar las características (normalización)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Paso 4: Definir el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(13, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Paso 5: Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Paso 6: Entrenar el modelo
history = model.fit(X_train, y_train, epochs=600, validation_data=(X_test, y_test), verbose=1)

# Paso 7: Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Model Test Accuracy: {accuracy:.4f}')

# Paso 8: Hacer predicciones y evaluar el rendimiento
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Reporte de clasificación
print(classification_report(y_test, y_pred))

# Matriz de confusión
print(confusion_matrix(y_test, y_pred))

# Paso 9: Visualización de los resultados (opcional)
# Graficar la precisión y la pérdida durante el entrenamiento
import matplotlib.pyplot as plt

# Precisión del entrenamiento y validación
plt.plot(history.history['accuracy'], label='Entrenamiento')
plt.plot(history.history['val_accuracy'], label='Validación')
plt.title('Precisión del Modelo')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend()
plt.show()

# Pérdida del entrenamiento y validación
plt.plot(history.history['loss'], label='Entrenamiento')
plt.plot(history.history['val_loss'], label='Validación')
plt.title('Pérdida del Modelo')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend()
plt.show()
