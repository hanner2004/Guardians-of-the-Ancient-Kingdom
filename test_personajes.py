
```python
"""Pruebas de las clases del reino de Eldoria."""

import pytest

from personajes import Personaje, Guerrero, Mago, Arquero, Combate


def test_crear_guerrero():
    personaje = Guerrero("Aldric", 120, 32, 18)

    assert personaje.nombre == "Aldric"
    assert personaje.vida == 120
    assert personaje.ataque == 32
    assert personaje.defensa == 18


def test_crear_mago():
    personaje = Mago("Lyra", 95, 38, 12)

    assert personaje.nombre == "Lyra"
    assert personaje.vida == 95
    assert personaje.ataque == 38
    assert personaje.defensa == 12


def test_crear_arquero():
    personaje = Arquero("Eiden", 105, 34, 14)

    assert personaje.nombre == "Eiden"
    assert personaje.vida == 105
    assert personaje.ataque == 34
    assert personaje.defensa == 14


def test_nombre_vacio():
    with pytest.raises(ValueError):
        Guerrero("", 100, 20, 5)


def test_vida_fuera_de_rango():
    with pytest.raises(ValueError):
        Guerrero("Aldric", 130, 20, 5)


def test_ataque_cero():
    with pytest.raises(ValueError):
        Guerrero("Aldric", 100, 0, 5)


def test_defensa_negativa():
    with pytest.raises(ValueError):
        Guerrero("Aldric", 100, 20, -1)


def test_recibir_impacto():
    personaje = Guerrero("Aldric", 100, 20, 10)

    impacto = personaje.recibir_impacto(30)

    assert impacto == 30
    assert personaje.vida == 70


def test_vida_no_baja_de_cero():
    personaje = Guerrero("Aldric", 10, 20, 5)

    impacto = personaje.recibir_impacto(50)

    assert impacto == 10
    assert personaje.vida == 0


def test_ataque_guerrero():
    atacante = Guerrero("Aldric", 100, 32, 10)
    rival = Guerrero("Guardia", 100, 15, 10)

    impacto = atacante.ejecutar_habilidad(rival)

    assert impacto == 26
    assert rival.vida == 74


def test_ataque_mago():
    atacante = Mago("Lyra", 95, 38, 12)
    rival = Guerrero("Guardia", 120, 15, 10)

    impacto = atacante.ejecutar_habilidad(rival)

    assert impacto == 35
    assert rival.vida == 85


def test_ataque_arquero():
    atacante = Arquero("Eiden", 105, 34
