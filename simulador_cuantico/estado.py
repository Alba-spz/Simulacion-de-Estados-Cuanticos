import math
from typing import List, Union

class EstadoCuantico:
    def __init__(self, id: str, vector: List[Union[float, complex]], base: str = "computacional"):
        if not id:
            raise ValueError("El identificador del estado cuántico no puede estar vacío.")
        if not vector or len(vector) == 0:
            raise ValueError("El vector de estado no puede estar vacío.")

        self.id = id
        self.vector = vector
        self.base = base

        if not self._esta_normalizado():
            raise ValueError(f"El vector no está normalizado: suma de probabilidades = {self._norma_cuadrada():.4f}")

    def _norma_cuadrada(self) -> float:
        """Calcula la norma cuadrada del vector: suma de |amplitud|^2."""
        return sum(abs(comp)**2 for comp in self.vector)

    def _esta_normalizado(self, tolerancia: float = 1e-6) -> bool:
        """Verifica si el vector está normalizado dentro de una tolerancia numérica."""
        return abs(self._norma_cuadrada() - 1.0) <= tolerancia

    def medir(self) -> dict:
        """
        Calcula las probabilidades de medición como |amplitud|^2 para cada componente.
        Retorna un diccionario que mapea cada estado base con su probabilidad.
        """
        probabilidades = {}
        for i, amplitud in enumerate(self.vector):
            prob = abs(amplitud)**2
            base_str = str(i)
            probabilidades[base_str] = round(prob, 4)  # Redondeamos para presentación
        return probabilidades

    def __str__(self) -> str:
        return f"{self.id}: vector={self.vector} en base {self.base}"

    def __repr__(self) -> str:
        return self.__str__()