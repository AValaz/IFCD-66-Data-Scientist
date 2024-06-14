## ejercicio 73

def tablas():
    n, m = int(input("dime un número del 1 al 10: ")), int(input("dime otro número del 1 al 10: "))
    try:
        with open(f"tabla-{n}.txt", 'r', encoding='utf8') as f:
            return f.readlines()[m]
    except FileNotFoundError:
        return f"tabla-{n}.txt no se encuentra disponible"
    
print(tablas())