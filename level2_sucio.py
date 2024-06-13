def aplicacion(f = "seno" , n=90):
    """
    USO: Aplica una funcion a un numero
    PARAMETROS:
        f[str]: funcion a aplicar
        n[int]: numero a evaluar
    VARIABLES:
        funciones[dict]: recupera la instruccion de math en funcion de f
        resultado[dict]: almacena la aplicacion de la funcion matematica al rango valores de 1 hasta n
    RETURN:
        pd[float]: el valor evaluacion de la funcion al numero
    """
    funciones = {'seno':sin, 'coseno':cos, 'tangente':tan, 'exponencial':exp, 'logarimo':log}
    resultado = {}
    for i in range(1,n+1):
        resultado[i] = funciones[f](i*pi/180)
    return resultado



def calculadora():
    """
    USO: 
    VARIABLES:
        f[str]: funcion a aplicar
        n[int]: numero a evaluar
        tx[str]: cadena que proporciona valor y evaluacion de la funcion
    FUNCIONES:
        aplicacion[fun]: Aplica una funcion a un numero
    RETURN:
        tx[str]: cadena que proporciona valor y evaluacion de la funcion 
    """
    print(f"Funciones disponibles: seno, coseno, tangente, exponencial, logaritmo")
    tx , f , n = "" , input("Funcion: ") , int(float(input("Numero: ")))
    for i , j in aplicacion(f , n).items():
        tx += f"{i:.2f}\t{j:.3f}\n"
    return tx
r = calculadora()
print(r)