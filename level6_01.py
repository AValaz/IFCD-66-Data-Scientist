# ejercicio 1

divisas = {'Euro':'€', 'Dollar':'$', 'Yen': '¥' }

respuesta = input("Dime una divisa: ")

if respuesta in divisas:
    print(f"El símbolo correspondiente a esa divisa es {divisas[respuesta]}")
else:
    print("Esa divisa no está en nuestra base de datos")