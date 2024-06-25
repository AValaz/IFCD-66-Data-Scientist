## Ejercicio 128
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def grafico(s, g):
    fig, ax = plt.subplots()
    if g == 'lineas':
        ax.plot(range(len(s)), list(s.values()))
        plt.xticks(range(len(s)), list(s.keys()))
    if g == 'barras':
        ax.bar(range(len(s)), list(s.values()))
        plt.xticks(range(len(s)), list(s.keys()))
    if g == 'sectores':
        ax.pie(list(s.values()), labels=list(s.keys()), autopct='%1.1f%%', startangle=90)
    if g == 'areas':
        ax.fill_between(range(len(s)), list(s.values()))
        plt.xticks(range(len(s)), list(s.keys()))
    plt.title('Evolución del número de ventas')
    plt.show()

ventas = {2019:10, 2020: 5, 2021:3}
g = 'sectores'
grafico(ventas, g)
