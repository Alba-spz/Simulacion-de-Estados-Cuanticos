class EstadoCuantico:
    def __init__(self, identificador, vector_estado, base="computacional"):
        self.identificador = identificador
        self.vector = vector_estado  # Lista de amplitudes (floats o complex)
        self.base = base

    def medir(self):
        """Devuelve un diccionario con las probabilidades de colapsar en cada estado base."""
        total = sum(abs(a) ** 2 for a in self.vector)
        return {f"|{i}>": abs(a) ** 2 / total for i, a in enumerate(self.vector)}

    def __str__(self):
        return f"{self.identificador}: {self.vector} en base {self.base}"

    def __repr__(self):
        return self.__str__()
