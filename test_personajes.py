import pytest
from personajes import Personaje, Guerrero, Mago, Arquero, Combate


def test_creacion_tres_personajes():
    assert Guerrero("A", 100, 30, 10).esta_vivo()
    assert Mago("B", 80, 40, 5).esta_vivo()
    assert Arquero("C", 90, 35, 15).esta_vivo()


@pytest.mark.parametrize("constructor,args", [
    (Guerrero, ("", 50, 10, 0)),
    (Mago, ("Merlín", 101, 10, 0)),
    (Arquero, ("Legolas", -1, 10, 0)),
    (Guerrero, ("Thor", 50, 0, 0)),
    (Mago, ("Mira", 50, -2, 0)),
    (Arquero, ("Naira", 50, 10, -1)),
])
def test_rechaza_datos_invalidos(constructor, args):
    with pytest.raises((TypeError, ValueError)):
        constructor(*args)


def test_guerrero_potencia_ataque_y_redondea_hacia_abajo():
    atacante = Guerrero("Bruno", 100, 30, 0)
    objetivo = Guerrero("Rival", 100, 10, 10)
    assert atacante.atacar(objetivo) == 26
    assert objetivo.vida == 74


def test_mago_ignora_defensa():
    atacante = Mago("Luna", 80, 40, 0)
    objetivo = Guerrero("Rival", 100, 10, 99)
    assert atacante.atacar(objetivo) == 40
    assert objetivo.vida == 60


def test_arquero_critico_y_sin_ventaja():
    arquero = Arquero("Naira", 90, 35, 0)
    rival = Guerrero("Rival", 100, 10, 15)
    assert arquero.atacar(rival) == 40

    arquero_sin_ventaja = Arquero("Prueba", 90, 10, 0)
    rival_fuerte = Guerrero("Fuerte", 100, 10, 10)
    assert arquero_sin_ventaja.atacar(rival_fuerte) == 0


def test_vida_no_baja_de_cero_y_devuelve_danio_efectivo():
    personaje = Guerrero("Defensor", 10, 5, 0)
    assert personaje.recibir_danio(40) == 10
    assert personaje.vida == 0


def test_no_se_acepta_danio_negativo():
    personaje = Guerrero("Defensor", 10, 5, 0)
    with pytest.raises(ValueError):
        personaje.recibir_danio(-1)


def test_personaje_derrotado_no_ataca():
    atacante = Guerrero("Caído", 0, 20, 0)
    objetivo = Mago("Rival", 50, 10, 0)
    with pytest.raises(ValueError):
        atacante.atacar(objetivo)


def test_combate_identifica_ganador():
    guerrero = Guerrero("Fuerte", 100, 100, 0)
    mago = Mago("Mago", 10, 1, 0)
    combate = Combate(guerrero, mago)
    resultado = combate.iniciar(mostrar=False)
    assert "Ganador: Fuerte" == resultado
    assert combate.ganador is guerrero


def test_empate_tecnico_si_una_ronda_no_causa_danio():
    primero = Guerrero("Roble", 100, 5, 100)
    segundo = Guerrero("Piedra", 100, 5, 100)
    combate = Combate(primero, segundo)
    resultado = combate.iniciar(mostrar=False)
    assert "Empate técnico" in resultado


def test_combate_rechaza_mismo_objeto():
    personaje = Guerrero("Uno", 50, 10, 5)
    with pytest.raises(ValueError):
        Combate(personaje, personaje)
