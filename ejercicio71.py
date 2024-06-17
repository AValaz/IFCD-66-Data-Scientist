## Ejercicio 71

def multp():
    c = True

    while c:
        numero = int(input("Número entero del 1 al 10: "))
        if 0<= numero <= 10:
            c = False
        else:
            numero = int(input("Número entero del 1 al 10: "))

    with open(f"salidas\\tabla-{numero}.txt", 'w', encoding='utf8') as f:
        for i in range(0, 11):
            f.write(f"{numero}x{i} = {numero*i}\n")


print(multp())