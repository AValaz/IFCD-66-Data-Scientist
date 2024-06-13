## ejercicio 3

precios = {'plátano': 1.35, "manzana": 0.80, "pera" : 0.85, "naranja":0.70}

fruta = input("Dime una fruta: ").lower()
kilos = float(input("Dime un número de kg: "))

if fruta in precios:
    print(f"El precio a pagar será {precios[fruta]*kilos} euros")
else:
    print("La fruta no está disponible")


