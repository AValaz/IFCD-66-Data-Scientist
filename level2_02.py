## Ejercicio 2
from math import sin, cos, tan, exp, log

def calculadora (f, n):
    func = input("Dime que función quieres que aplique: ")
    numero = input("Dime el valor entero: ")
    """
    Applying IVA on a price
    Parameters: 
        n[int]: number to evaluate
        f[str]: function to apply
    Variables:
        funciones[dict]: recupera la instrucción en función de f
        resultado[dict]: almacena función matemática y su resultado de 1 a n
    Returns:     
        precio_final: precio con el IVA aplicado
    """
    funciones = {"seno": sin, "coseno": cos, "tangente": tan, "exponencial":exp, "logaritmo": log}
    resultado = {}
    for i in range(1, n+1):
        resultado[i] = funciones[f](i)

    return resultado    


