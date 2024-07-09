## Supongamos que el número anual de accidentes de tránsito en el tramo de autopista
## entre Vinarós y Oropesa sigue una distribución de Poisson con parámetro l=10 accidentes
## por año

# a) Cual es la probabilidad de observar exactamente 10 accidentes en 1995

from scipy.stats import poisson
# lambda_ = 10
# pisson_dist = poisson(lambda_)
# prob_acc = pisson_dist.pmf(10)
#print(f"Probabilidad de observar exactamente 10 accidentes en 1995: {prob_acc}")


#b) Cual es la probabilidad de observar exactamente 35 accidentes entre el 1 de enero de 1995 y el 31 de diciembre de 1996
# lambda_ = 20
# pisson_dist = poisson(lambda_)
# prob_acc = pisson_dist.pmf(35)
# print(f"Probabilidad de observar exactamente 35 accidentes entre el 1 de enero de 1995 y el 31 de diciembre de 1996: {prob_acc*100:.2f}%")

# c) Se rediseña y señaliza el trazado de la autopista y en los siguientes 2 años se
# observan 12 accidentes ¿Se ha mejorado frente a la situación anterior?(Cual era la
# probabilidad de haber observado 12 o menos accidentes)
# lambda_ = 20
# pisson_dist = poisson(lambda_)
# prob_12_o_menos = pisson_dist.cdf(12)
# print(f"Probabilidad de observar probabilidad de haber observado 12 o menos accidentes en dos años: {prob_12_o_menos*100:.2f}%")


# La incidencia anual por VIH+ en los toxicómanos de la Comunidad Valenciana es de 12
# por100 toxicomanos. Si se toma una muestra de 30 toxicomanos seronegativos y se sigue
# a lo largo del año
from scipy.stats import binom
# a) Cual es la probabilidad de observar al menos 4 casos en un año
p, n = 12/100, 30
prob_menos_4 = binom.cdf(3,n,p)
prob_al_menos_4 = 1 - prob_menos_4

print(f"Probabilidad de observar al menos 4 casos en un año: {prob_al_menos_4*100:.2f}%")

# c) Cual seria el número esperado de infecciones: 3.6 infecciones.

# 8.- Si la cantidad de colesterol en sangre en una variable normalmente distribuida, con
# media de 200mg/100ml y desviación típica 20mg/100ml, obtener la probabilidad de que
# un individuo elegido al azar posea una cantidad de colesterol
from scipy.stats import norm
# me = 200
# des = 20
# colesterol = norm(me,des)

# a) Menor de 150mg/100ml
# prob_colest_menores_150 = colesterol.cdf(150)
# print(f"Probabilidad de colesterol menor a 150mg/100ml: {prob_colest_menores_150*100:.2f}%")

# b) Mayor de 180mg/100ml
# prob_colest_menores_180 = colesterol.cdf(180)
# prob_colest_mayores_180 = 1-prob_colest_menores_180
# print(f"Probabilidad de colesterol mayores a 180mg/100ml: {prob_colest_mayores_180*100:.2f}%")

# c) Entre 180mg/100ml y 200mg/100ml
# prob_colest_menores_200 = colesterol.cdf(200)
# prob_colest_menores_180 = colesterol.cdf(180)
# prob_colest_entre_180_200 = prob_colest_menores_200-prob_colest_menores_180
# print(f"Probabilidad de colesterol entre 180mg/100ml y 200mg/100ml: {prob_colest_entre_180_200*100:.2f}%")

# d) Obten los percentiles 5,10,25,50,76,90,95 de la distribución


# El Indice de masa corporal (peso/talla2) de una población sigue una distribución normal
# con media 25.2 y desviación típica de 2.8. Se considera delgados a aquellos que su IMC
# esta por debajo de 20 y obesos a aquellos que su IMC esta por encima de 30. ¿Cual es la
# proporción de delgados y obesos de la población?. Calcula los percentiles 5 y 95 de dicha
# distribución.

# me = 25.2
# des = 2.8
# imc = norm(me,des)

# prob_imc_menores_20 = imc.cdf(20)
# prob_imc_menores_30 = imc.cdf(30)
# prob_imc_mayores_30 = 1- imc.cdf(30)
# print(f"Probabilidad de imc menores a 20: {prob_imc_menores_20:.2f}% y Probabilidad de imc mayores a 30: {prob_imc_mayores_30:.2f}%")

# percentil_5 = imc.ppf(0.05)
# percentile_9 = imc.ppf(0.05)

# En una población se pretende llevar a cabo un programa de educación sanitaria sobre la
# hiperuricemia. Se sabe que el nivel de ácido úrico en la población sigue una distribución
# normal con media 6 mg y desviación típica 1,1 mg. Si unicamente se puede atender al
# 10% de la población que valor de ácido úrico se debe seleccionar para elegir al 10% de la
# población con mayor nivel de ácido úrico.

# me = 6
# des = 1.1
# ac_urico = norm(me,des)
# percentile_90 = ac_urico.ppf(0.90)
# print(f"10% de la población con mayor nivel de ácido úrico son aquellos cuyo ácido urico está por encima de {percentile_90:.2f}mg")




