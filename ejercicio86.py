## Ejercicio 86

from itertools import permutations

palabras = ["alo", "tio", "veo"]

permutaciones = {palabra:[''.join(p) for p in permutations(palabra)] for palabra in palabras}

print(permutaciones)