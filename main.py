

"""Programa principal del reino de Valdoria."""

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
    print("LAS CRÓNICAS DEL REINO DE VALDORIA")
    print("=" * 40)

    print("\n1. Creación de personajes")

    guardia = Centinela("Aldric", 115, 30, 16)
    invocadora = Hechicero("Lyra", 90, 36, 11)
    rastreador = Explorador("Eiden", 100, 32, 13)

    for personaje in (guardia, invocadora, rastreador):
        print(personaje.mostrar_datos())

    print("\n2. Prueba de habilidades")

    objetivo = Centinela("Centinela de práctica", 120, 14, 10)

    impacto = guardia.ejecutar_habilidad(objetivo)
    print(f"Impacto de Aldric: {impacto}")

    objetivo.energia = 120
    impacto = invocadora.ejecutar_habilidad(objetivo)
    print(f"Impacto de Lyra: {impacto}")

    objetivo.energia = 120
    objetivo.resistencia = 14
    impacto = rastreador.ejecutar_habilidad(objetivo)
    print(f"Impacto de Eiden: {impacto}")

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
        lambda: guardia.recibir_impacto(-3),
    )

    print("\n4. Comprobación de energía mínima")

    resistente = Centinela("Durnak", 10, 5, 2)
    impacto_real = resistente.recibir_impacto(50)

    print(f"Impacto efectivo: {impacto_real}")
    print(f"Energía restante: {resistente.energia}")

    print("\n5. Duelo entre personajes")

    aldric = Centinela("Aldric", 115, 30, 16)
    lyra = Hechicero("Lyra", 90, 36, 11)

    duelo = GestorDuelo(aldric, lyra)
    print(duelo.iniciar())

    print("\n6. Prueba de empate técnico")

    primero = Centinela("Piedra Gris", 100, 5, 100)
    segundo = Centinela("Muro del Norte", 100, 5, 100)

    empate = GestorDuelo(primero, segundo)
    print(empate.iniciar())


if __name__ == "__main__":
    ejecutar_programa()


