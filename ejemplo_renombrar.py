## Comprobar: 
import time
import numpy as np
import pandas as pd
import math

n = 10**6 ## 10**9 con int64
## sin(k3*pi/180)*(e**k-1/log(k))

def calculo_pandas(k):
    try:
        r = math.sin(k*math.pi/180)*(math.e**k-1/math.log(k))
        if math.isinf(r) or math.isnan(r):
            return -9999
        else:
            return r
    except:
        return -9999

def calculo_numpy(k):
    with np.errstate(divide = 'ignore', invalid='ignore', over = 'ignore'):
        r = np.sin(k*np.pi/180)*(np.exp(k)-(1/np.log10(k)))
        r[np.isinf(r)] = -9999
        r[np.isnan(r)] = -9999
    return r

## Listas Python
lista_python = list(range(1, n))
start1 = time.time()
result = map(calculo_pandas, lista_python)
lista_result_python = list(result)
end1 = time.time()
result1 = end1-start1
del(start1, end1, lista_python, lista_result_python)

## Listas Numpy
lista_numpy = np.arange(1, n, dtype=np.int64)
start2 = time.time()
lista_result_numpy = calculo_numpy(lista_numpy)
end2 = time.time()
result2 = end2-start2
del(start2, end2, lista_numpy, lista_result_numpy)

## Series Pandas
lista_pandas = pd.Series(range(1,n), dtype='int64')
start3 = time.time()
list_result_pandas = lista_pandas.apply(calculo_pandas)
end3 = time.time()
result3 = end3-start3
del(start3, end3, lista_pandas)


print(f"La lista nativa de Python tarda {result1}")
print(f"La lista de Numpy tarda {result2}")
print(f"Las series de Pandas tarda {result3}")