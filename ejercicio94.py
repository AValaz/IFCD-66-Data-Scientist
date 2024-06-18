# Ejercicio 94

lista_C = [25, 75.2, 100]

convertir = lambda x: x*1.8+32

clasificar = lambda f: "Frio" if f<50 else "Templado" if 50<=f<=85 else "Calor"

for x in lista_C:
    print(clasificar(convertir(x)))