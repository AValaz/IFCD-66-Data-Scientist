# Genera una matriz 10×10 donde cada elemento es un número primo. Usa una lista de comprensión anidada.

list_prime = []

for num in range(0, 100 + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           list_prime.append(num)


matriz = [[i for i in list_prime[0:10]] for j in list_prime[0:10]]
print(matriz)