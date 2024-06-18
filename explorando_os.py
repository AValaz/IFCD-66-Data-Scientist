## Explorando la Librería os en Python
import os
import platform
import time
import stat

## 1. Información del Sistema:
# print(os.name)
# print(platform.system())
# print(os.getlogin())
# print(os. getcwd())

##2. Manipulación de Directorios:
# base_dir = "C:\\Users\\Ale\\Documents\\IronHack\\Git"
# test_os = "C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os"
# os.mkdir(test_os) ## Crea nuevo directorio
# os.chdir(test_os) ## Cambia el directorio de trabajo
#os.chdir("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os")
# dir1 = "C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\dir1"
# dir2 = "C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\dir2"
# dir3 = "C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\dir3"
# os.mkdir(dir1)
# os.mkdir(dir2)
# os.mkdir(dir3)

#print(os.listdir()) # Listamos tods los archivos y directorios del directorio actual

## 3. Manipulación de Archivos:
#Crear archivo example.txt
# test_os = "C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example.txt"
# if os.path.exists(test_os):
#     print('Ya existe el archivo')
# else:
#     with open(test_os, 'w') as f:
#         # uncomment if you want empty file
#         f.write('')

# Renombrar
# os.rename("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example1.txt", "C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example1.txt")

# Copiar un archivo a otro
# with open("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example1.txt", 'r') as origen:
#     with open("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example2.txt", 'w') as destino:
#         destino.write(origen.read())

# Borrar archivo
# os.remove("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example1.txt")

## 4. Información sobre Archivos y Directorios:
# Tamaño de example2.txt
# print( os.path.getsize("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example2.txt"))

# Fecha de creación del archivo
# print(time.ctime(os.path.getctime("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example2.txt")))

# Comprueba si example2.txt es un archivo y si dir1 es un directorio.
# print(os.path.isfile("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example2.txt"))
# print(os.path.isdir("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\dir1"))

## 5. Permisos y Propiedades de Archivos:
# Cambia los permisos de example2.txt para que sea solo lectura.
os.chmod("C:\\Users\\Ale\\Documents\\IronHack\\Git\\test_os\\example2.txt", stat.S_IRUSR) 


## 6. Operaciones del Sistema:
# Ejecuta un comando del sistema, como listar los archivos en el directorio (ls en Unix o dir en Windows).
#print(os.system('dir'))

# Crea una variable de entorno personalizada.
# os.environ['saludo'] = 'hola'
# print(os.environ['saludo'])

## 7. Manejo de Rutas:
# Unir varias partes de una ruta de archivo:
directorio = 'C:\\Users\\Ale\\Documents\\IronHack\\Git'
subdirectorio = 'test_os'
archivo = 'example2.txt'

ruta_completa = os.path.join(directorio, subdirectorio, archivo)

# Dividir una ruta en el nombre del directorio y el nombre del archivo:
# print(os.path.dirname(ruta_completa))
# print(os.path.basename(ruta_completa))

# Obtener el nombre base y la extensión de un archivo a partir de una ruta completa:
print(os.path.splitext(ruta_completa)[-1])

