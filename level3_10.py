# Ejercicio 10
x = input("Dime los productos que has comprado, separdos por comas: ")

for product in list(x.split(',')):
    print(product.lstrip())
