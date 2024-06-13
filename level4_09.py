## ejercicio 9
contrasenya = "hola"
while True:
    prueba = input("Dime la contraseña: ")
    if prueba == contrasenya:
        print("Puedes pasar, contraseña correcta")
        break
    else:
        print("Introduce la contraseña correcta! ")
