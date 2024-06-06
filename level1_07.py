# Ejercicio 7

x = float(input("Dime tu peso en kg: "))
y = float(input("Dime tu estatura en m: "))

print(f"Tu IMC es {round((x/y**2),2)}")