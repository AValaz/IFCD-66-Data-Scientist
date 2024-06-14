## ejercicio 72

def multp():
    numero = int(input("Número entero del 1 al 10: "))
    try:
        with open(f"tabla-{numero}.txt", 'r', encoding='utf8') as f:
            return f.read()
    except FileNotFoundError:
        return f"tabla-{numero}.txt no se encuentra disponible"

print(multp())

