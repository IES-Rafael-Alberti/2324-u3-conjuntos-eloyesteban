"""
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""

def definir_conjunto_numeros():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    return numeros

def numeros_pares(numeros):
    pares = {numero for numero in numeros if numero % 2 == 0}
    return pares

def numeros_multiplos_de_tres(numeros):
    multiplos_de_tres = {numero for numero in numeros if numero % 3 == 0}
    return multiplos_de_tres

def interseccion(pares, multiplos):
    interseccion_set = pares.intersection(multiplos)
    return interseccion_set
    
if __name__ == "__main__":

    numeros = definir_conjunto_numeros()

    pares = numeros_pares(numeros)

    multiplos = numeros_multiplos_de_tres(numeros)

    interseccion_set = interseccion(pares, multiplos)

    print("Conjunto de Pares:", pares)
    print("Conjunto de Múltiplos de Tres:", multiplos)
    print("Intersección entre Pares y Múltiplos de Tres:", interseccion_set)

