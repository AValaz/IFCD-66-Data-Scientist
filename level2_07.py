## Ejercicio 7


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
        dict_final[k.upper()] = calif(v)
        dict_final
    return dict_final

dict_ejemplo = {"Ale":5, "Mari":6, "Javi":3.5}

pruebas = calificaciones(dict_ejemplo)
print(pruebas)
