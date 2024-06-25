## Ejercicio 130

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bancos = pd.read_csv('C:\\Users\\Ale\\Documents\\IronHack\\Git\\salidas\\bancos.csv', index_col = 'Fecha', parse_dates= True)

fig, ax = plt.subplots(figsize=(10, 6))
empresas = bancos['Empresa'].unique()


for empresa in empresas:
        df_empresa = bancos[bancos['Empresa'] == empresa]
        ax.plot(df_empresa.index, df_empresa['Cierre'], label=empresa)

ax.set_title('Series temporales de las cotizaciones de cierre de cada banco')
ax.set_xlabel('Fecha')
ax.set_ylabel('Cotización de cierre')
ax.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()