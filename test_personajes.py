
import pytest

from personajes import (
    Combatiente,
    Centinela,
    Hechicero,
    Explorador,
    GestorDuelo,
)


def test_creacion_de_combatientes():
    assert Centinela("A", 120, 30, 10).sigue_en_pie()
    assert Hechicero("B", 90, 40, 5).sigue_en_pie()
    assert Explorador("C", 100, 35, 15).sigue_en_pie()


def test_clase_base_es_abstracta():
    with pytest.raises(TypeError):
        Combatiente("Base", 100, 20, 5)


@pytest.mark.parametrize("constructor,datos", [
    (Centinela, ("", 50, 10, 0)),
    (Hechicero, ("Selene", 121, 10, 0)),
    (Explorador, ("Kael", -1, 10, 0)),
    (Centinela, ("Darian", 50, 0, 0)),
    (Hechicero, ("Lira", 50, -2, 0)),
    (Explorador, ("Nox", 50, 10, -1)),
])
def test_rechaza_datos_invalidos(constructor, datos):
    with pytest.raises((TypeError, ValueError)):
        constructor(*datos)


def test_centinal_aumenta_el_poder():
    atacante = Centinela("Darian", 100, 30, 5)
    rival = Centinela("Rival", 100, 10, 10)

    impacto = atacante.ejecutar_habilidad(rival)

    assert impacto == 24
    assert rival.energia == 76


def test_hechicero_reduce_parte_de_la_resistencia():
    atacante = Hechicero("Selene", 90, 40, 5)
    rival = Centinela("Rival", 100, 10, 99)

    impacto = atacante.ejecutar_habilidad(rival)

    assert impacto == 7
    assert rival.energia == 93


def test_explorador_aprovecha_debilidades():
    explorador = Explorador("Kael", 100, 35, 5)
    rival = Centinela("Rival", 100, 10, 15)

    impacto = explorador.ejecutar_habilidad(rival)

    assert impacto == 28
    assert rival.energia == 72


def test_explorador_no_supera_defensa_alta():
    explorador = Explorador("Kael", 100, 10, 5)
    rival = Centinela("Baluarte", 100, 10, 20)

    impacto = explorador.ejecutar_habilidad(rival)

    assert impacto == 0
    assert rival.energia == 100


def test_energia_no_baja_de_cero():
    luchador = Centinela("Bastión", 10, 5, 0)

    assert luchador.recibir_impacto(40) == 10
    assert luchador.energia == 0


def test_no_acepta_impacto_negativo():
    luchador = Centinela("Bastión", 10, 5, 0)

    with pytest.raises(ValueError):
        luchador.recibir_impacto(-1)


def test_derrotado_no_puede_atacar():
    atacante = Centinela("Caído", 0, 20, 0)
    rival = Hechicero("Selene", 50, 10, 0)

    with pytest.raises(ValueError):
        atacante.ejecutar_habilidad(rival)


def test_gestor_identifica_ganador():
    fuerte = Centinela("Titán", 100, 100, 0)
    debil = Hechicero("Aprendiz", 10, 1, 0)

    duelo = GestorDuelo(fuerte, debil)
    resultado = duelo.iniciar(mostrar=False)

    assert resultado == "Ganador del duelo: Titán"
    assert duelo.ganador is fuerte


def test_empate_tecnico():
    primero = Centinela("Muralla", 100, 5, 100)
    segundo = Centinela("Rocafirme", 100, 5, 100)

    duelo = GestorDuelo(primero, segundo)
    resultado = duelo.iniciar(mostrar=False)

    assert "Empate técnico" in resultado


def test_no_puede_enfrentarse_a_si_mismo():
    luchador = Centinela("Darian", 50, 10, 5)

    with pytest.raises(ValueError):
        GestorDuelo(luchador, luchador)

