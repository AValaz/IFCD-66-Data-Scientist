## ejercicio 9

palabra = input("Dime una palabra: ")

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in palabra:
    if letra.lower() == 'a':
        contador_a+=1
    
print(f"La palabra {palabra} tiene {contador_a} a")