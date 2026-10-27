

```python
"""Programa principal del reino de Eldoria."""

from personajes import (
    Guerrero,
    Mago,
    Arquero,
    Combate,
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

    print("\n1. Creación de personajes")

    guerrero = Guerrero("Aldric", 120, 32, 18)
    mago = Mago("Lyra", 95, 38, 12)
    arquero = Arquero("Eiden", 105, 34, 14)

    for personaje in (guerrero, mago, arquero):
        print(personaje.mostrar_datos())

    print("\n2. Prueba de habilidades")

    objetivo = Guerrero("Guardia de prueba", 120, 15, 10)

    impacto = guerrero.ejecutar_habilidad(objetivo)
    print(f"Impacto del Guerrero: {impacto} (esperado: 26)")

    objetivo.vida = 120
    impacto = mago.ejecutar_habilidad(objetivo)
    print(f"Impacto del Mago: {impacto} (esperado: 35)")

    objetivo.vida = 120
    objetivo.defensa = 14
    impacto = arquero.ejecutar_habilidad(objetivo)
    print(f"Impacto del Arquero: {impacto} (esperado: 28)")

    print("\n3. Validación de datos")

    comprobar_error(
        "Nombre vacío",
        lambda: Guerrero("", 100, 20, 5),
    )

    comprobar_error(
        "Vida superior al límite",
        lambda: Mago("Prueba", 130, 20, 5),
    )

    comprobar_error(
        "Ataque igual a cero",
        lambda: Arquero("Prueba", 80, 0, 5),
    )

    comprobar_error(
        "Defensa negativa",
        lambda: Guerrero("Prueba", 80, 20, -1),
    )

    comprobar_error(
        "Impacto negativo",
        lambda: guerrero.recibir_impacto(-3),
    )

    print("\n4. Comprobación de vida mínima")

    resistente = Guerrero("Bastión", 10, 5, 2)
    impacto_real = resistente.recibir_impacto(50)

    print(f"Impacto efectivo: {impacto_real}")
    print(f"Vida restante: {resistente.vida}")

    print("\n5. Combate entre dos personajes")

    aldric = Guerrero("Aldric", 120, 32, 18)
    lyra = Mago("Lyra", 95, 38, 12)

    combate = Combate(aldric


