# ejercicio 96

productos = [
    {'nombre': 'Producto A', 'precio': 150, 'cantidad': 30},
    {'nombre': 'Producto B', 'precio': 85, 'cantidad': 50},
    {'nombre': 'Producto C', 'precio': 120, 'cantidad': 5},
    {'nombre': 'Producto D', 'precio': 200, 'cantidad': 20},
    {'nombre': 'Producto E', 'precio': 75, 'cantidad': 40},
    {'nombre': 'Producto F', 'precio': 110, 'cantidad': 15}
]

filtro = lambda x: x['precio']>100 and x['cantidad']>10

resultado = list(filter(filtro, productos))

ordenado = sorted(resultado, key=lambda x: x['precio'], reverse=True)

print(ordenado)