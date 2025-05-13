import numpy as np
from .estado import EstadoCuantico

class OperadorCuantico:
    def __init__(self, nombre, matriz):
        self.nombre = nombre
        self.matriz = np.array(matriz, dtype=complex)

    def aplicar(self, estado: EstadoCuantico, nuevo_id=None):
        """Devuelve un nuevo EstadoCuantico al aplicar la operación a un estado dado."""
        nuevo_vector = np.dot(self.matriz, np.array(estado.vector))
        nuevo_id = nuevo_id or f"{estado.identificador}_{self.nombre}"
        return EstadoCuantico(nuevo_id, nuevo_vector.tolist(), estado.base)
