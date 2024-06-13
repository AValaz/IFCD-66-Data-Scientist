## ejercicio 7

abecedario = ["abcdefghijklmnñopqrstuvwxyz"]
list_abecedario = list(abecedario[0])

nuevo_abecedario = [letra for i, letra in enumerate(list_abecedario) if (i + 1) % 3 != 0]

print(nuevo_abecedario)