
```python
"""Clases principales del reino de Eldoria."""

from abc import ABC, abstractmethod


class Personaje(ABC):
    """Clase abstracta que representa a un personaje."""

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
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("La vida debe ser un número entero.")
        if not 0 <= valor <= 120:
            raise ValueError("La vida debe estar entre 0 y 120.")
        self.__vida = valor

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("El ataque debe ser un número entero.")
        if valor <= 0:
            raise ValueError("El ataque debe ser mayor que cero.")
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

    def recibir_impacto(self, cantidad):
        """Reduce la vida y devuelve el daño efectivo."""
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("El impacto debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("El impacto no puede ser negativo.")

        anterior = self.vida
        self.vida = max(0, self.vida - cantidad)
        return anterior - self.vida

    def sigue_en_pie(self):
        return self.vida > 0

    def mostrar_datos(self):
        return (
            f"{self.nombre} ({type(self).__name__}) | "
            f"Vida: {self.vida} | Ataque: {self.ataque} | "
            f"Defensa: {self.defensa}"
        )

    def validar_rival(self, rival):
        if not isinstance(rival, Personaje):
            raise TypeError("El rival debe ser un personaje válido.")
        if not self.sigue
        return self.mostrar_resultado()

