# Ejercicio 4

x = input("Dime tu número de teléfono en formato prefijo-número-extensión: ")

print(f"Tu número de teléfono sin prefijo ni extensión es {x.split('-')[1]}")