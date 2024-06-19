"""
"""

c, o = {}, '' #diccionario clientes, opción

while o != '6':
    if o == '1':        # preguntar datos y añadirlos
        nif, n, d, t, e, v = '54859632M', 'jose', 'Carrer Tuset', '652658698', 'jose@gmail.com', True ##input("Nif: "), input("Nombre: "), input("Dirección: "), input("Teléfono: "), input("email: "), bool(input("VIP?: "))  
        c[nif] = {'Nombre': n, 'Dirección': d, "Teléfono":t, 'email': e, 'VIP': v}
    elif o == '2':      # eliminar por nif
        nif = '54859632M' ##input("Nif: ")
        if nif in c:
            del c[nif]
        else:
            print(f"No existe el nif {nif} en la BBDD")
    elif o == '3':      # mostrar datos por nif
        nif = '54859632M' ##input("Nif: ")
        print(f"Los datos asociados a este nif son {c[nif]}")
    elif o == '4':      # listar clientes con nif y nombre
        for k in c:
            print (f"el Nif es {k} y su nombre es {c[k]['Nombre']}")
    else:      # mostrar VIP
        for i, j in c.items():
            if j['VIP'] == True:
                print(f"{c[i]['Nombre']} es VIP")

    print("1.Añadir usuarios \n 2.Eliminar usuarios\n 3.Mostrar datos por nif \n 4.Mostrar todos los clientes \n 5.Mostrar VIPS")
    o = input('Qué hacemos?').strip()
