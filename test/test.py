from src.main import Bowls

def test_bolera():
    assert 30 == Bowls("X111111111111111111").calcular_puntos()
    assert 60 == Bowls("12345123451234512345").calcular_puntos()
    assert 90 == Bowls("9-9-9-9-9-9-9-9-9-9-").calcular_puntos()
    assert 150 == Bowls('5/5/5/5/5/5/5/5/5/5/5').calcular_puntos()
    assert 175 == Bowls('X5/X5/XX5/--5/X5/').calcular_puntos()
    assert 120 == Bowls('XX9-9-9-9-9-9-9-9-').calcular_puntos()