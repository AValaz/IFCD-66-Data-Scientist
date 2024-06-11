## Ejercicio 8


def calif(nota):
    """
    USO: califica en base a unas notas
    PARÁMETROS: 
        nota[int/float]: nota de 0 a 10
    VARIABLES:
        c[int/float]: calificación cualitativa
    DEVOLUCION:     
        c[int/float]: calificación cualitativa
    """
    if nota<5:
        c = "suspenso"
    elif nota <7:
        c = "aprobado"
    elif nota <9:
        c = "notable"
    elif nota <10:
        c = "sobresaliente"
    elif nota == 10:
        c = "matrícula"
    return c

def calificaciones(dict):
    """
    Qualitative qulaifications
    Parameters: 
        dict[dictionary]: name and grades of each studen
    Variables:
        dict_final[dictionary]: empty.Where the qualitative qualifications will be
    Returns:     
        dict_final[dictionary]: empty.Where the qualitative qualifications will be
    """
    
    dict_final = {}
    for k, v in dict.items():
        if v >= 5:
            dict_final[k.upper()] = calif(v)
            dict_final
        else:
            pass
    return dict_final

dict_ejemplo = {"Javi":3.5, "Ale":5, "Mari":6}

pruebas = calificaciones(dict_ejemplo)
print(pruebas)
