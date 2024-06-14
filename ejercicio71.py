## Ejercicio 71

def multp():
    numero = int(input("Número entero del 1 al 10: "))
    with open(f"tabla-{numero}.txt", 'w', encoding='utf8') as f:
        for i in range(0, 11):
            f.write(f"{numero}x{i}= {numero*i}\n")


print(multp())