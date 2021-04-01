from src.main import Bolera

def test_bolera():
    assert 60 == Bolera("12345123451234512345").calcular_puntos()