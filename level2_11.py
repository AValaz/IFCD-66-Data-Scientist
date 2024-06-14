## Ejercicio 11
from statistics import mean, stdev
l = [1,2,3,4,5,6,7,8,9,10,100,1999]
media = mean(l)

def valores_atip(l):
    media = mean(l)
    desvs = stdev(l)

    def score(n):
        puntuacion = (n-media) / desvs
        return puntuacion<-3 or puntuacion>3    
    return score
    

def resol(L):
    return list(filter(valores_atip(L), L))


print(resol(l))