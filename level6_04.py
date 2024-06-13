## ejercicio 4
meses = {'01':'enero', '02': 'febrero', '03':'marzo'}

fecha = input("Dime una fecha en formato dd/mm/aaaa ")

lista_fecha = fecha.split('/')

print(f"{lista_fecha[0]} de {meses[lista_fecha[1]]} de {lista_fecha[2]}")