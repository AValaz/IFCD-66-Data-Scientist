# Supongamos que una empresa quiere comprobar si el tiempo promedio que tardan sus
# empleados en completar una tarea específica es diferente de 30 minutos. Se toma una
# muestra aleatoria de cincuenta empleados y se mide el tiempo que tardan en completar
# la tarea. Realiza un contraste de hipótesis para determinar si el tiempo promedio que
# tardan los empleados en completar la tarea es diferente de 30 minutos, utilizando un nivel
# de significancia del 5%.

import numpy as np
from scipy import stats

# # H0 = tiempo promedio es igual a 30 minutos
# np.random.seed(42)
# muestra = np.random.normal(loc=32, scale=5, size=50)

# media_esperada = 30

# t_stat , p_value = stats.ttest_1samp(muestra, media_esperada)
# print(f"Estadístico t: {t_stat}")
# print(f"Valor p: {p_value}")

# alpha = 0.05
# if p_value < alpha:
#     print("Rechazamos la hipótesis nula (H0)")
# else:
    # print("No rechazamos la hipótesis nula (H0)")


# Un investigador quiere determinar si hay una diferencia significativa en los niveles de
# colesterol entre dos grupos de pacientes: un grupo que sigue una dieta especial y otro
# grupo que no la sigue. Se toman muestras de ambos grupos y se miden sus niveles de
# colesterol. Realiza un contraste de hipótesis para determinar si hay una diferencia
# significativa en los niveles de colesterol entre los dos grupos, utilizando un nivel de
# significancia del 5%.

# H0 = no hay diferencia entre los grupos que hacen dieta y los que no
# np.random.seed(42)
# muestra_dieta = np.random.normal(loc=180, scale=15, size=30)
# muestra_sin_dieta = np.random.normal(loc=190, scale=20, size=30)

# t_stat , p_value = stats.ttest_ind(muestra_sin_dieta, muestra_dieta,  equal_var=False)
# print(f"Estadístico t: {t_stat}")
# print(f"Valor p: {p_value}")

# alpha = 0.05
# if p_value < alpha:
#     print("Rechazamos la hipótesis nula (H0), Acepto H1<> NO hay diferencia significativa")
# else:
#     print("No rechazamos la hipótesis nula (H0)")

# Un investigador desea verificar si la proporción de estudiantes que aprueban un examen
# es mayor al 60%. Se toma una muestra aleatoria de 100 estudiantes y se registra si
# aprobaron o no el examen. Realiza un contraste de hipótesis para determinar si la
# proporción de estudiantes que aprueban el examen es mayor al 60%, utilizando un nivel
# de significancia del 5%.

# Datos:
# • Generaremos los datos asumiendo que la verdadera proporción de aprobados es
# del 65%.
# • Utilizar semilla aleatoria fijada en 42.

from scipy.stats import binom
from statsmodels.stats.proportion import proportions_ztest
np.random.seed(42)
# Parámetros
p, p0A, n = 1, 65/100, 100
aprobados = np.random.binomial(p,p0A,n)

p0 = 60/100
alpha = 5/100
t_stat , p_value = proportions_ztest(aprobados.sum(), n, p0, alternative = 'larger')

# Una fábrica quiere comprobar si la variabilidad en el peso de sus productos es diferente a
# 2 gramos2. Se toma una muestra aleatoria de cuarenta productos y se mide su peso.
# Realiza un contraste de hipótesis para determinar si la varianza en el peso de los
# productos es diferente a 2 gramos2, utilizando un nivel de significancia del 5%.

# Datos:
# • Los datos de la muestra son de carácter normal, y son generados con una varianza
# real de 2.5 gramos2 y media 50.
# • Utilizar semilla aleatoria fijada en 42.

# H0 = la variabilidad del peso no es diferente a 2 gramos
# np.random.seed(42)
# muestra = np.random.normal(loc=50, scale=2.5, size=40)

# media_esperada = 200

# t_stat , p_value = stats.ttest_1samp(muestra, media_esperada)
# print(f"Estadístico t: {t_stat}")
# print(f"Valor p: {p_value}")

# alpha = 0.05
# if p_value < alpha:
#     print("Rechazamos la hipótesis nula (H0)")
# else:
#     print("No rechazamos la hipótesis nula (H0)")