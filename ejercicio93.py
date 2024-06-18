# Ejercicio 93
descuento = lambda x: x*0.90 if x>100 else x*0.95

lista_precios = [95, 110, 150, 50]

for x in lista_precios:
    print(descuento(x))