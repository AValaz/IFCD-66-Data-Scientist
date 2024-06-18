# Ejercicio 95

lista_ingresos = [25000, 45000, 125000]

clasificar = lambda x: "Bajo" if x<30000 else "Medio" if 30000<=x<=70000 else "Alto"

for x in lista_ingresos:
    print(clasificar(x))