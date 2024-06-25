## Ejercicio 125
import matplotlib.pyplot as plt
import numpy as np

def grafico (dict, c):
    fig, ax = plt.subplots()
    plt.bar(range(len(notas)), list(notas.values()), align='center', color = c)
    plt.xticks(range(len(notas)), list(notas.keys()))
    plt.show()

notas = {'matematicas':10, 'biología': 5, 'inglés':3}
color = 'red'

grafico(notas, color)