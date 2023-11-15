"""
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.

"""

def definir_alfabeto():
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    return alfabeto

def definir_vocales():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    return vocales

def letras_comunes(vocales, alfabeto):
    letras_comunes = vocales.intersection(alfabeto)
    return letras_comunes

if __name__ == "__main__":
    # Procesar
    alfabeto = definir_alfabeto()
    vocales = definir_vocales()
    letras_comunes_set = letras_comunes(vocales, alfabeto)
    consonantes = alfabeto - vocales

    # Salida
    print("Conjunto de Consonantes:", consonantes)
    print("Conjunto de Letras Comunes:", letras_comunes_set)
