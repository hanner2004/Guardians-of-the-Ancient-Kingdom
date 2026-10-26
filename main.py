"""Demostración del proyecto y comprobaciones manuales solicitadas."""
from personajes import Personaje, Guerrero, Mago, Arquero, Combate


def probar_validacion(etiqueta, funcion):
    try:
        funcion()
    except (TypeError, ValueError) as error:
        print(f"[CORRECTO] {etiqueta}: {error}")
    else:
        print(f"[REVISAR] {etiqueta}: se esperaba una excepción.")


def ejecutar_demostracion():
    print("GUARDIANS OF THE ANCIENT KINGDOM")
    print("1. Creación de los tres tipos")
    guerrero = Guerrero("Bruno", 100, 30, 20)
    mago = Mago("Luna", 80, 40, 10)
    arquero = Arquero("Naira", 90, 35, 15)
    for personaje in (guerrero, mago, arquero):
        print(personaje.mostrar_estado())

    print("\n2. Habilidades especiales")
    objetivo = Guerrero("Objetivo", 100, 10, 10)
    danio_guerrero = guerrero.atacar(objetivo)
    print(f"Daño del Guerrero: {danio_guerrero} (esperado: 26)")

    objetivo.vida = 100
    danio_mago = mago.atacar(objetivo)
    print(f"Daño del Mago: {danio_mago} (esperado: 40)")

    objetivo.vida = 100
    objetivo.defensa = 15
    danio_arquero = arquero.atacar(objetivo)
    print(f"Daño del Arquero: {danio_arquero} (esperado: 40)")

    print("\n3. Validaciones")
    probar_validacion("nombre vacío", lambda: Guerrero("  ", 100, 20, 5))
    probar_validacion("vida mayor que 100", lambda: Mago("Prueba", 101, 20, 5))
    probar_validacion("ataque cero", lambda: Arquero("Prueba", 80, 0, 5))
    probar_validacion("defensa negativa", lambda: Guerrero("Prueba", 80, 20, -1))
    probar_validacion("daño negativo", lambda: guerrero.recibir_danio(-3))

    print("\n4. La vida no baja de cero")
    resistente = Guerrero("Escudo", 10, 5, 2)
    danio_real = resistente.recibir_danio(50)
    print(f"Daño efectivo: {danio_real}; vida final: {resistente.vida}")

    print("\n5. Combate completo")
    arthas = Guerrero("Arthas", 100, 30, 20)
    gandalf = Mago("Gandalf", 80, 40, 10)
    combate = Combate(arthas, gandalf)
    print(combate.iniciar())

    print("\n6. Empate técnico")
    defensor_a = Guerrero("Roble", 100, 5, 100)
    defensor_b = Guerrero("Piedra", 100, 5, 100)
    empate = Combate(defensor_a, defensor_b)
    print(empate.iniciar())

    print("\nNota: las pruebas automatizadas están en test_personajes.py.")


if __name__ == "__main__":
    ejecutar_demostracion()
