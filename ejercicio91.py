mayor_edad = lambda edad: edad>18

lista_edades = [18, 5, 25, 35, 91]

aplicar = filter(mayor_edad, lista_edades)

for x in aplicar:
    print(x)
