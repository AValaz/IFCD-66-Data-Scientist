## ejercicio 6

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

def calificaciones (lista):
    for i in lista:
        return [calif(i) for i in lista]

lista_ejemplo = [5, 6, 10, 4.5]

print(calificaciones(lista_ejemplo))

