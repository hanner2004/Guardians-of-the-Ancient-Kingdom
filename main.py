
"""Programa principal del reino de Eldoria."""

from personajes import (
    Centinela,
    Hechicero,
    Explorador,
    GestorDuelo,
)


def comprobar_error(descripcion, accion):
    try:
        accion()
    except (TypeError, ValueError) as error:
        print(f"[CORRECTO] {descripcion}: {error}")
    else:
        print(f"[ERROR] No se detectó el problema: {descripcion}")


def ejecutar_programa():
    print("EL REINO DE ELDORIA")
    print("=" * 35)

    print("\n1. Creación de combatientes")

    centinela = Centinela("Darian", 120, 32, 18)
    hechicero = Hechicero("Selene", 95, 38, 12)
    explorador = Explorador("Kael", 105, 34, 14)

    for luchador in (centinela, hechicero, explorador):
        print(luchador.mostrar_datos())

    print("\n2. Prueba de habilidades")

    objetivo = Centinela("Guardia de prueba", 120, 15, 10)

    impacto = centinela.ejecutar_habilidad(objetivo)
    print(f"Impacto del Centinela: {impacto} (esperado: 26)")

    objetivo.energia = 120
    impacto = hechicero.ejecutar_habilidad(objetivo)
    print(f"Impacto del Hechicero: {impacto} (esperado: 35)")

    objetivo.energia = 120
    objetivo.resistencia = 14
    impacto = explorador.ejecutar_habilidad(objetivo)
    print(f"Impacto del Explorador: {impacto} (esperado: 28)")

    print("\n3. Validación de datos")

    comprobar_error(
        "Nombre vacío",
        lambda: Centinela("", 100, 20, 5),
    )

    comprobar_error(
        "Energía superior al límite",
        lambda: Hechicero("Prueba", 130, 20, 5),
    )

    comprobar_error(
        "Poder igual a cero",
        lambda: Explorador("Prueba", 80, 0, 5),
    )

    comprobar_error(
        "Resistencia negativa",
        lambda: Centinela("Prueba", 80, 20, -1),
    )

    comprobar_error(
        "Impacto negativo",
        lambda: centinela.recibir_impacto(-3),
    )

    print("\n4. Comprobación de energía mínima")

    resistente = Centinela("Bastión", 10, 5, 2)
    impacto_real = resistente.recibir_impacto(50)

    print(f"Impacto efectivo: {impacto_real}")
    print(f"Energía restante: {resistente.energia}")

    print("\n5. Duelo entre dos combatientes")

    darian = Centinela("Darian", 120, 32, 18)
    selene = Hechicero("Selene", 95, 38, 12)

    duelo = GestorDuelo(darian, selene)
    print(duelo.iniciar())

    print("\n6. Prueba de empate técnico")

    primero = Centinela("Muralla", 100, 5, 100)
    segundo = Centinela("Rocafirme", 100, 5, 100)

    empate = GestorDuelo(primero, segundo)
    print(empate.iniciar())


if __name__ == "__main__":
    ejecutar_programa()

