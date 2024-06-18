"""
Función general que engloba 4 subfunciones que permiten crear un listín telefónico, añadir un teléfono, eliminar un usuario
y borrar o crear un listín.
"""
import os 

def recuperarTelefono(f, c): 
    """
    USO: devuelve el teléfono del cliente en el fichero
    PARAMETROS:
        f[str]: fichero de teléfono - cliente
        c[str]: nombre del cliente
    VARIABLES:
        c[list]: lectura de fichero nombre-tfno
        x[str]: diccionario nom-telefono/ advertencia si no existe el nombre de la persona
    RETURN:
        x[str]: diccionario nom-telefono/ advertencia si no existe el nombre de la persona

    """
    try:
        with open(f) as F:
            c = F.readlines()
    except FileNotFoundError:
        x = 'Archivo no encontrado'
    else:
        x = dict([tuple(k.split(',')) for k in c])

    return x

def anadirTelefono(f, nc, tc):
    """
    USO: añade el teléfono del cliente en el fichero
    PARAMETROS:
        f[str]: fichero de teléfono - cliente
        nc[str]: nombre del cliente
        tc[str]: telefono del cliente
    VARIABLES:
        F[list]: lectura de fichero nombre-tfno
        x[str]: diccionario nom-telefono/ advertencia si no existe el nombre de la persona
    RETURN:
        y[str]: nombre cliente y su telefono
        x[str]: advertencia escritura

    """
    try:
        F = open(f, 'a', encoding='utf8')
    except FileNotFoundError:
        x = 'Archivo no encontrado'
    else:
        y = f"{nc},{tc}\n"
        F.write(y)
        x = f"Se ha añadido el {nc} con el teléfono {tc} a {f}"
        F.close()

def eliminarTelefono (f,nc):
    """
    USO: elimina el teléfono del cliente en el fichero
    PARAMETROS:
        f[str]: fichero de teléfono - cliente
        nc[str]: nombre del cliente
    VARIABLES:
        F[list]: lectura de fichero nombre-tfno
        p[list/dict]: líneas de la lectura del archivo por cada índice del list que muta a un diccionario 
                    cuya clave es el nombre tras procesar el list anterior
        x[str]: diccionario nom-telefono/ advertencia si no existe el nombre de la persona
    RETURN:
        y[str]: nombre cliente y su telefono
        x[str]: advertencia escritura

    """
    try:
        F = open(f, 'r', encoding='utf8')
    except FileNotFoundError:
        x = 'Archivo no encontrado'
    else:
        p = F.readlines()
        F.close()
        p = dict([tuple(k.split(',')) for k in p])
        if nc in p:
            print("El cliente existe")
            del p[nc]
            F = open(f, 'w', encoding='utf8')
            for i, j in p.items():
                y = f"{i},{j}"
                F.write(y)
                x = f"Se ha eliminado el cliente {nc} del fichero {f}"

                F.close()
        else:
            x = f"El cliente {nc} no existen en el fichero {f}"

def borrarArchivo(f):
    if os.path.isfile(f): #archivo existe
        r = input("El archivo existe, ¿Borramos el archivo? (S/N): ")
        if r == "S":
            try:
                os.remove(f)
            #f = open(f, 'w') #Se sobrescribe el archivo y lo deja en blanco
            #f.close()
                x = "Se ha borrado el archivo"
            except FileNotFoundError:
                x = "No existe el fichero o la uri es invalida"
            except PermissionError:
                x = "No tienes privilegios para borrar ese fichero"
            except Exception as error:
                x = f"Se ha producido un error desconocido. \n Se ha producido el error: {error}"
        else:
            x = "No se ha borrado el archivo"
    else:
        h = input ("El archivo no existe \n. ¿Quieres crear un fichero (S-N): ?").upper()
        if h == 'S':
            with open(f, 'w', encoding = 'utf8') as F:
                c = F.write('')
            x = "Se ha creado el archivo"
        else:
            x = "No se ha creado el fichero"
    return x

def menu(f):
    qh = input("Qué quieres hacer?: ")
    if qh == "1":
        op = input("Nombre a consultar: ").strip()
        y = recuperarTelefono(f, op)
    elif qh == "2":
        op = input("Añadir nombre-telefono: ").strip()
        n, t = op.split('-')[0], op.split('-')[1]
        y = anadirTelefono(f, op.split)
    elif qh == "3":
        op = input("Nombre a eliminar: ").strip()
        y = eliminarTelefono (f,op)
    elif qh == "4":
        op = input("Directorio del fichero: ").strip()
        y = borrarArchivo(f)
    else:
        y = "Bye"
    return y        

print("""
1: Mirar teléfono
2: Añadir teléfono
3: Eliminar teléfono
4: Crear fichero
0/5: Terminar
""")

F = "salidas\\listin.txt"

print(menu(F))