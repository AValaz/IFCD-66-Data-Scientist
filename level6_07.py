## ejercicio 7
diccionario = {}

while True:
    x = input("Dime sobre que campo me vas a dar info y si quieres terminar, simplemente escribe 'terminar': ")

    if x=='terminar':
        break

    y = input(f"Dime la info sobre {x}: ")
    diccionario[x] = y

print(diccionario)
