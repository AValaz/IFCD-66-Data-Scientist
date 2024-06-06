# Ejercicio 12

x = int(input("Barras que no son del día: "))

#Precio de la barra normalmente
y = 3.49

print(f"El precio de una barra de pan es de {y} euros al no ser frescas, el precio queda en {round(y*0.4, 2)} y como solo quedan {x} barras, el precio total de las barras son {y*0.4*x} euros")