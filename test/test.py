from src.main import Bowls

def test_bolera():
    assert 30 == Bowls("X111111111111111111").calcular_puntos()
    assert 61 == Bowls("12345123451234512346").calcular_puntos()