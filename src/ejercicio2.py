"""
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

    Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
    Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
    Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
    Mostrar si todos los nombres de primaria están incluidos en secundaria.

"""

def cargar_nombres(alumnos):
    nombre = input("Nombre: ")
    while nombre.lower() != "x":
        alumnos.add(nombre)
        nombre = input("Nombre: ")
    return alumnos

primaria = set()
secundaria = set()

print("ALUMNOS DE PRIMARIA")
primaria = cargar_nombres(primaria)

print("ALUMNOS DE SECUNDARIA")
secundaria = cargar_nombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria | secundaria:
    print(nombre)

print("NOMBRES COMUNES:")
for nombre in primaria & secundaria:
    print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria - secundaria:
    print(nombre)
print("¿ESTAN LOS NOMBRES DE PRIMARIA INCLUIDOS EN SECUNDARIA?")
todos_en_secundaria = primaria.issubset(secundaria)
print(todos_en_secundaria)


