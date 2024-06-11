## Ejercicio 1

# Función 1
def descuento(p, d):
    """
    Applying a discount on a price
    Parameters: 
        p[int/float]: original price of the product
        d[int/float]: discount to apply in percentage
    Variables:
        precio_final[float]: precio con el descuento aplicado
    Returns:     
        precio_final: precio con el descuento aplicado
    """
    precio_final = p*(1-d/100) 
    return precio_final



# Función 2
def aplicar_iva(p, iva):
    """
    Applying IVA on a price
    Parameters: 
        p[int/float]: original price of the product
        iva[int/float]: IVA to be applied
    Variables:
        precio_final[float]: precio con el IVA aplicado
    Returns:     
        precio_final: precio con el IVA aplicado
    """
    precio_final = p*(1+iva/100) 
    return precio_final

# Función 3
def cesta (func, productos):
    total_compra = 0
    if func == "descuento":
        for key, value in productos.items():
            total_compra+=descuento(key, value)

    else:
        for key, value in productos.items():
            total_compra+=aplicar_iva(key, value)

    return total_compra
