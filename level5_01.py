## ejercicio 1

list_asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print(list_asignaturas)

# for asignatura in list_asignaturas:
#     print(asignatura)

## ejercicio 2 
# for asignatura in list_asignaturas:
#      print(f"Yo estudio {asignatura}")

## ejercicio 3
notas={}

for asignatura in list_asignaturas:
   nota = input(f"Qué nota has sacado en {asignatura}? ")
   notas[asignatura] = nota

for k,v in notas.items():
   print(f"En {k} he sacado {v}")
