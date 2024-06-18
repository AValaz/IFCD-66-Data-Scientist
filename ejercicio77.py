## Ejercicio 77

def diccionario(f):
    try:
        with open(f, 'r', encoding='utf8') as file:
            lineas = file.readlines()
            cabecera = lineas[0].strip().split(';')
            data_dict = {col: [] for col in cabecera}

            for linea in lineas[1:]:
                valores = linea.strip().split(';')
                for col, valores in zip(cabecera, valores):
                    data_dict[col].append(valores)
            return data_dict
               
        
    except FileNotFoundError:
        print("Fichero no encontrado")


archivo = "C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\cotizacion.csv"

print(diccionario(archivo))