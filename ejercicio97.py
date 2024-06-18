## ejercicio 97

empleados = [
    {'nombre': 'Juan', 'salario': 50000, 'departamento': 'Ventas'},
    {'nombre': 'Ana', 'salario': 60000, 'departamento': 'Marketing'},
    {'nombre': 'Luis', 'salario': 75000, 'departamento': 'IT'},
    {'nombre': 'Marta', 'salario': 45000, 'departamento': 'RRHH'}
]

impuesto = lambda x: x['salario']*0.10 

for x in empleados:
    x['impuesto']=impuesto(x)
