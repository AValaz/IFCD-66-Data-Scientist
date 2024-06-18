import csv

archivo = "C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\calificaciones.csv"

def notas(archivo):
    lista_diccionarios = []
    with open(archivo) as f:
        csv_reader = csv.DictReader(f, delimiter = ';')
        for i in csv_reader:
            lista_diccionarios.append({'Apellidos':i['Apellidos'], 'Asistencia':i['Asistencia'], 'Parcial1':i['Parcial1'], 'Parcial2':i['Parcial2'], 'Practicas':i['Practicas']})

    ordenado = sorted(lista_diccionarios, key=lambda d: d['Apellidos'])
    return ordenado

lista_pruebas = notas(archivo)

for i in lista_pruebas:
    i['Nota final'] = float(i['Parcial1'])*0.3 + float(i['Parcial1'])*0.3 + float(i['Practicas'])*0.4 

print(lista_pruebas)

    # for k, v in i.items():
    #     print(f'{k} and {v}')