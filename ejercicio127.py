## Ejercicio 127
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def trimestre (series, t):
    fig, ax = plt.subplots()
    meses = ['mes1', 'mes2', 'mes3']
    ax.pie(series, labels = meses)
    plt.title(f'{t}')
    plt.savefig('C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\meses.png')
    plt.show()


ventas = [150,85,269]
ventas = pd.Series(ventas)

trimestre(ventas, 'Distribución de ventas en los diferentes meses del trimestre')