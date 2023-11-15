from src.ejercicio5 import definir_conjunto_numeros,numeros_pares, numeros_multiplos_de_tres, interseccion

def test_definir_conjunto_numeros():
    numeros = definir_conjunto_numeros()
    assert isinstance(numeros, set)
    assert len(numeros) == 10
    assert 1 in numeros
    assert 10 in numeros

def test_numeros_pares():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares = numeros_pares(numeros)
    assert isinstance(pares, set)
    assert len(pares) == 5
    assert 2 in pares
    assert 8 in pares

def test_numeros_multiplos_de_tres():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    multiplos_de_tres = numeros_multiplos_de_tres(numeros)
    assert isinstance(multiplos_de_tres, set)
    assert len(multiplos_de_tres) == 3
    assert 3 in multiplos_de_tres
    assert 9 in multiplos_de_tres


