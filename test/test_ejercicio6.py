from src.ejercicio6 import definir_alfabeto, definir_vocales, letras_comunes

def test_definir_alfabeto():
    alfabeto = definir_alfabeto()
    assert isinstance(alfabeto, set)
    assert len(alfabeto) == 26
    assert 'a' in alfabeto
    assert 'z' in alfabeto

def test_definir_vocales():
    vocales = definir_vocales()
    assert isinstance(vocales, set)
    assert len(vocales) == 5
    assert 'a' in vocales
    assert 'u' in vocales

def test_letras_comunes():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    letras_comunes_set = letras_comunes(vocales, alfabeto)

    assert isinstance(letras_comunes_set, set)
    assert len(letras_comunes_set) == 5
    assert 'a' in letras_comunes_set
    assert 'e' in letras_comunes_set
    assert 'i' in letras_comunes_set
    assert 'o' in letras_comunes_set
    assert 'u' in letras_comunes_set
