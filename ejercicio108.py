## Ejercicio 108
# 3x+4y-z=1
# 2x-y+3z=4
# 5x+2y+2z=-1
import numpy as np

a = np.array([[3,4,-1],[2,-1,3],[5,2,2]])
b = np.array([1,4,-1])
x = np.linalg.solve(a, b)

print(x)