## Ejemplo 129

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

meses = ['ene', 'feb','mar','abr', 'may','jun']
ingresos = [1000,2220,3255,4100,5822,1000]
gastos = [500,780,523,547,159,658]
columns = ['meses', 'ingresos', 'gastos']
df_ejemplo = pd.DataFrame(list(zip(meses, ingresos, gastos)), columns=columns)

# def diagrama(df):
fig, ax = plt.subplots()
ax.plot(df_ejemplo['meses'], df_ejemplo['ingresos'], label = 'ingresos')
ax.plot(df_ejemplo['meses'], df_ejemplo['gastos'], label='gastos')
plt.title('Evolución de ingresos y gastos')
plt.legend(loc="upper left")
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
plt.show()
