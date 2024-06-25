## Ejercicio 126
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def notas(serie):
    fig, ax = plt.subplots()
    ax.boxplot(serie)
    plt.title('Distribución de notas')
    plt.show()

lista_notas = [5,6,8,7.5,9]
serie = pd.Series(lista_notas)
notas(serie)