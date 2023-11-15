"""
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
    Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
    Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
    Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.

"""

def definir_set_frutas1():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    set_frutas1 = set(frutas1)
    return set_frutas1

def definir_set_frutas2():
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas2 = set(frutas2)
    return set_frutas2

def encontrar_frutas_comunes(set_frutas1, set_frutas2):
    frutas_comunes = set_frutas1.intersection(set_frutas2)
    return frutas_comunes

def encontrar_frutas_solo_conjuntos(set_frutas1, set_frutas2):
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1
    return frutas_solo_en_frutas1, frutas_solo_en_frutas2

if __name__ == "__main__":
    # Procesar
    set_frutas1 = definir_set_frutas1()
    set_frutas2 = definir_set_frutas2()
    frutas_comunes = encontrar_frutas_comunes(set_frutas1, set_frutas2)
    frutas_solo_en_frutas1, frutas_solo_en_frutas2 = encontrar_frutas_solo_conjuntos(set_frutas1, set_frutas2)

    # Salida
    print("Conjunto de Frutas 1:", set_frutas1)
    print("Conjunto de Frutas 2:", set_frutas2)
    print("Frutas Comunes:", frutas_comunes)
    print("Frutas Solo en Frutas 1:", frutas_solo_en_frutas1)
    print("Frutas Solo en Frutas 2:", frutas_solo_en_frutas2)

