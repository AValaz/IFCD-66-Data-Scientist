## ejercicio 2
nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
direccion = input("Dime tu direccion: ")

dict = {"nombre": nombre, "edad": edad, "dirección": direccion}

print(f"{dict['nombre']} tiene {dict['edad']} y vive en {dict['dirección']}")