#ejercico 5

asignaturas = {'Matemáticas': 6, "Física": 4, "Química":5}
suma = 0

for k, v in asignaturas.items():
    print(f"{k} tiene {v}")
    suma+= v

#print(f"{sum(asignaturas.values())} en total")  #Opción 1
# print(f"{suma} en total") #Opción 2