## Ejercicio 84

def divisores(n)_
    return[i for i in range (1, n) if n%i == 0]

def perfecto(n):
    return(sum(divisores(n))) == n

numeros_perfectos = [i for n in range(1,1000) if perfecto(n)]