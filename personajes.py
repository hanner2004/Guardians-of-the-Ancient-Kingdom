"""Clases del sistema Guardians of the Ancient Kingdom.

Este módulo define los personajes y el administrador del combate.
No ejecuta demostraciones ni pruebas al importarse.
"""
from abc import ABC, abstractmethod


class Personaje(ABC):
    """Clase base abstracta para todos los guardianes."""

    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        self.__nombre = valor.strip()

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("La vida debe ser un número entero.")
        if not 0 <= valor <= 100:
            raise ValueError("La vida debe estar entre 0 y 100.")
        self.__vida = valor

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("El ataque debe ser un número entero.")
        if valor <= 0:
            raise ValueError("El ataque debe ser positivo.")
        self.__ataque = valor

    @property
    def defensa(self):
        return self.__defensa

    @defensa.setter
    def defensa(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("La defensa debe ser un número entero.")
        if valor < 0:
            raise ValueError("La defensa no puede ser negativa.")
        self.__defensa = valor

    def recibir_danio(self, cantidad):
        """Aplica un daño ya calculado y devuelve el daño efectivo."""
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("El daño debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("El daño no puede ser negativo.")

        vida_anterior = self.vida
        self.vida = max(0, self.vida - cantidad)
        return vida_anterior - self.vida

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_estado(self):
        return (
            f"{self.nombre} ({self.__class__.__name__}) | "
            f"Vida: {self.vida} | Ataque: {self.ataque} | "
            f"Defensa: {self.defensa}"
        )

    def _validar_objetivo(self, objetivo):
        if not isinstance(objetivo, Personaje):
            raise TypeError("El objetivo debe ser un personaje válido.")
        if not self.esta_vivo():
            raise ValueError(f"{self.nombre} no puede atacar porque está derrotado.")
        if not objetivo.esta_vivo():
            raise ValueError(f"{objetivo.nombre} ya está derrotado.")

    @abstractmethod
    def atacar(self, objetivo):
        """Calcula y aplica el ataque propio de cada clase."""
        raise NotImplementedError


class Guerrero(Personaje):
    """Guardián que aumenta su ataque un 20 %."""

    def atacar(self, objetivo):
        self._validar_objetivo(objetivo)
        ataque_potenciado = (self.ataque * 120) // 100
        danio = max(0, ataque_potenciado - objetivo.defensa)
        return objetivo.recibir_danio(danio)


class Mago(Personaje):
    """Guardián cuyos hechizos ignoran la defensa."""

    def atacar(self, objetivo):
        self._validar_objetivo(objetivo)
        return objetivo.recibir_danio(self.ataque)


class Arquero(Personaje):
    """Guardián que duplica el daño si supera la defensa rival."""

    def atacar(self, objetivo):
        self._validar_objetivo(objetivo)
        if self.ataque > objetivo.defensa:
            danio_base = self.ataque - objetivo.defensa
            danio = danio_base * 2
        else:
            danio = 0
        return objetivo.recibir_danio(danio)


class Combate:
    """Administra los turnos de dos personajes creados previamente."""

    MAX_RONDAS = 50

    def __init__(self, personaje_a, personaje_b):
        if not isinstance(personaje_a, Personaje) or not isinstance(personaje_b, Personaje):
            raise TypeError("El combate necesita dos objetos Personaje.")
        if personaje_a is personaje_b:
            raise ValueError("Un personaje no puede combatir contra sí mismo.")
        self.personajes = [personaje_a, personaje_b]
        self.indice_turno = 0
        self.rondas = 0
        self.ganador = None
        self.resultado = None

    @property
    def atacante_actual(self):
        return self.personajes[self.indice_turno]

    @property
    def objetivo_actual(self):
        return self.personajes[1 - self.indice_turno]

    def cambiar_turno(self):
        self.indice_turno = 1 - self.indice_turno

    def verificar_ganador(self):
        vivos = [personaje for personaje in self.personajes if personaje.esta_vivo()]
        if len(vivos) == 1:
            self.ganador = vivos[0]
            self.resultado = f"Ganador: {self.ganador.nombre}"
            return self.ganador
        if len(vivos) == 0:
            self.ganador = None
            self.resultado = "Empate: ambos personajes fueron derrotados."
            return None
        return None

    def mostrar_resultado(self):
        if self.resultado is None:
            return "El combate todavía no ha terminado."
        return self.resultado

    def iniciar(self, mostrar=True):
        """Ejecuta hasta 50 rondas; cada ronda tiene como máximo dos ataques."""
        if self.resultado is not None:
            return self.mostrar_resultado()

        if mostrar:
            print("\n=== COMIENZA EL COMBATE ===")
            for personaje in self.personajes:
                print(personaje.mostrar_estado())

        while self.rondas < self.MAX_RONDAS:
            danio_en_ronda = 0

            for _ in range(2):
                atacante = self.atacante_actual
                objetivo = self.objetivo_actual

                if not atacante.esta_vivo() or not objetivo.esta_vivo():
                    self.verificar_ganador()
                    break

                danio = atacante.atacar(objetivo)
                danio_en_ronda += danio

                if mostrar:
                    print(
                        f"\n{atacante.nombre} ataca a {objetivo.nombre} "
                        f"y causa {danio} de daño."
                    )
                    print(self.personajes[0].mostrar_estado())
                    print(self.personajes[1].mostrar_estado())

                if self.verificar_ganador() is not None or self.resultado is not None:
                    break

                self.cambiar_turno()

            self.rondas += 1

            if self.resultado is not None:
                break

            if danio_en_ronda == 0:
                self.resultado = "Empate técnico: una ronda completa sin causar daño."
                break

        if self.resultado is None:
            self.resultado = f"Empate: se alcanzó el límite de {self.MAX_RONDAS} rondas."

        if mostrar:
            print("\n" + self.mostrar_resultado())
        return self.mostrar_resultado()
