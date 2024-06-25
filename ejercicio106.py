## Ejercicio 106
import numpy as np

matriz_3D = np.random.randint(0, 100, (4, 3, 2))

print(f"La media es {matriz_3D.mean()}")
print(f"La media en el eje 0 es {matriz_3D.mean(axis=0)}")
print(f"La media en el eje 1 es {matriz_3D.mean(axis=1)}")
print(f"La media en el eje 2 es {matriz_3D.mean(axis=2)}")
print(f"La media en el eje 2 es {matriz_3D-matriz_3D.mean()}")