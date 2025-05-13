import numpy as np
from simulador_cuantico.estado import EstadoCuantico

class OperadorCuantico:
    def __init__(self, nombre: str, matriz):
        self.nombre = nombre
        self.matriz = np.array(matriz, dtype=complex)

        # Validación básica: matriz cuadrada
        if self.matriz.shape[0] != self.matriz.shape[1]:
            raise ValueError("La matriz del operador debe ser cuadrada.")

    def aplicar(self, estado: EstadoCuantico, nuevo_id: str = None) -> EstadoCuantico:
        vector_original = np.array(estado.vector, dtype=complex)

        # Validar dimensiones
        if self.matriz.shape[1] != vector_original.shape[0]:
            raise ValueError("Las dimensiones del operador y del estado no coinciden.")

        nuevo_vector = np.dot(self.matriz, vector_original)

        return EstadoCuantico(
            id=nuevo_id if nuevo_id else f"{estado.id}_{self.nombre}",
            vector=nuevo_vector.tolist(),
            base=estado.base
        )

    def __str__(self):
        return f"Operador {self.nombre}: matriz=\n{self.matriz}"
