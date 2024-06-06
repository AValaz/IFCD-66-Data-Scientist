# Ejercicio 11
x = float(input("Dime cuántos ahorros tienes: "))
# Tasa de interés
y = 0.04 
print(f"Tus ahorros el primer año serán {round(x*1.04, 2)} euros, el segundo año serán de {round(x*(1.04**2), 2)} euros y el tercer año de {round(x*(1.04**3), 2)} euros")