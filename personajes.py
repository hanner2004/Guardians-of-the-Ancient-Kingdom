
"""Clases principales del reino de Eldoria."""

from abc import ABC, abstractmethod


class Combatiente(ABC):
    """Clase abstracta que representa a un luchador del reino."""

    def __init__(self, nombre, energia, poder, resistencia):
        self.nombre = nombre
        self.energia = energia
        self.poder = poder
        self.resistencia = resistencia

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("La energía debe ser un número entero.")
        if not 0 <= valor <= 120:
            raise ValueError("La energía debe estar entre 0 y 120.")
        self.__energia = valor

    @property
    def poder(self):
        return self.__poder

    @poder.setter
    def poder(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("El poder debe ser un número entero.")
        if valor <= 0:
            raise ValueError("El poder debe ser mayor que cero.")
        self.__poder = valor

    @property
    def resistencia(self):
        return self.__resistencia

    @resistencia.setter
    def resistencia(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("La resistencia debe ser un número entero.")
        if valor < 0:
            raise ValueError("La resistencia no puede ser negativa.")
        self.__resistencia = valor

    def recibir_impacto(self, cantidad):
        """Reduce la energía y devuelve el impacto efectivo."""
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("El impacto debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("El impacto no puede ser negativo.")

        anterior = self.energia
        self.energia = max(0, self.energia - cantidad)
        return anterior - self.energia

    def sigue_en_pie(self):
        return self.energia > 0

    def mostrar_datos(self):
        return (
            f"{self.nombre} ({type(self).__name__}) | "
            f"Energía: {self.energia} | Poder: {self.poder} | "
            f"Resistencia: {self.resistencia}"
        )

    def validar_rival(self, rival):
        if not isinstance(rival, Combatiente):
            raise TypeError("El rival debe ser un combatiente válido.")
        if not self.sigue_en_pie():
            raise ValueError(f"{self.nombre} ya fue derrotado.")
        if not rival.sigue_en_pie():
            raise ValueError(f"{rival.nombre} ya está fuera de combate.")

    @abstractmethod
    def ejecutar_habilidad(self, rival):
        """Cada especialidad define su propia forma de atacar."""
        raise NotImplementedError


class Centinela(Combatiente):
    """Especialista en golpes físicos reforzados."""

    def ejecutar_habilidad(self, rival):
        self.validar_rival(rival)
        golpe = (self.poder * 115) // 100
        impacto = max(0, golpe - rival.resistencia)
        return rival.recibir_impacto(impacto)


class Hechicero(Combatiente):
    """Utiliza energía arcana para atravesar protecciones."""

    def ejecutar_habilidad(self, rival):
        self.validar_rival(rival)
        impacto = max(1, self.poder - rival.resistencia // 3)
        return rival.recibir_impacto(impacto)


class Explorador(Combatiente):
    """Busca puntos débiles para conseguir golpes precisos."""

    def ejecutar_habilidad(self, rival):
        self.validar_rival(rival)

        if self.poder >= rival.resistencia + 8:
            impacto = self.poder - rival.resistencia + 8
        else:
            impacto = max(0, self.poder - rival.resistencia)

        return rival.recibir_impacto(impacto)


class GestorDuelo:
    """Controla los turnos de dos combatientes."""

    LIMITE_RONDAS = 40

    def __init__(self, luchador_a, luchador_b):
        if not isinstance(luchador_a, Combatiente):
            raise TypeError("El primer luchador no es válido.")
        if not isinstance(luchador_b, Combatiente):
            raise TypeError("El segundo luchador no es válido.")
        if luchador_a is luchador_b:
            raise ValueError("Un luchador no puede enfrentarse a sí mismo.")

        self.luchadores = [luchador_a, luchador_b]
        self.turno = 0
        self.rondas = 0
        self.ganador = None
        self.resultado = None

    @property
    def luchador_actual(self):
        return self.luchadores[self.turno]

    @property
    def rival_actual(self):
        return self.luchadores[1 - self.turno]

    def cambiar_turno(self):
        self.turno = 1 - self.turno

    def comprobar_ganador(self):
        activos = [
            luchador for luchador in self.luchadores
            if luchador.sigue_en_pie()
        ]

        if len(activos) == 1:
            self.ganador = activos[0]
            self.resultado = f"Ganador del duelo: {self.ganador.nombre}"
            return self.ganador

        if len(activos) == 0:
            self.resultado = "Empate: ambos luchadores fueron derrotados."
            return None

        return None

    def mostrar_resultado(self):
        return self.resultado or "El duelo todavía no termina."

    def iniciar(self, mostrar=True):
        """Alterna los turnos hasta encontrar un resultado."""

        if self.resultado is not None:
            return self.mostrar_resultado()

        if mostrar:
            print("\n=== COMIENZA EL DUELO ===")
            for luchador in self.luchadores:
                print(luchador.mostrar_datos())

        while self.rondas < self.LIMITE_RONDAS:
            impacto_ronda = 0

            for _ in range(2):
                atacante = self.luchador_actual
                rival = self.rival_actual

                if not atacante.sigue_en_pie() or not rival.sigue_en_pie():
                    self.comprobar_ganador()
                    break

                impacto = atacante.ejecutar_habilidad(rival)
                impacto_ronda += impacto

                if mostrar:
                    print(
                        f"\n{atacante.nombre} utiliza su habilidad "
                        f"contra {rival.nombre} e inflige {impacto} puntos."
                    )
                    for luchador in self.luchadores:
                        print(luchador.mostrar_datos())

                self.comprobar_ganador()

                if self.resultado is not None:
                    break

                self.cambiar_turno()

            self.rondas += 1

            if self.resultado is not None:
                break

            if impacto_ronda == 0:
                self.resultado = (
                    "Empate técnico: nadie logró causar impacto."
                )
                break

        if self.resultado is None:
            self.resultado = (
                f"Empate: se alcanzó el límite de "
                f"{self.LIMITE_RONDAS} rondas."
            )

        if mostrar:
            print("\n" + self.mostrar_resultado())

        return self.mostrar_resultado()

