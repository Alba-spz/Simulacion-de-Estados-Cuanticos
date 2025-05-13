from .estado import EstadoCuantico
from .operador import OperadorCuantico

class RepositorioDeEstados:
    def __init__(self):
        self.estados = {}

    def listar_estados(self):
        return [str(estado) for estado in self.estados.values()]

    def agregar_estado(self, identificador, vector, base="computacional"):
        if identificador in self.estados:
            raise ValueError(f"Ya existe un estado con ID: {identificador}")
        self.estados[identificador] = EstadoCuantico(identificador, vector, base)

    def obtener_estado(self, identificador):
        return self.estados.get(identificador)

    def aplicar_operador(self, id_estado, operador: OperadorCuantico, nuevo_id=None):
        estado = self.obtener_estado(id_estado)
        if not estado:
            raise ValueError("Estado no encontrado")
        nuevo_estado = operador.aplicar(estado, nuevo_id)
        if nuevo_estado.identificador in self.estados:
            raise ValueError("El nuevo identificador ya existe")
        self.estados[nuevo_estado.identificador] = nuevo_estado
        return nuevo_estado

    def medir_estado(self, identificador):
        estado = self.obtener_estado(identificador)
        if not estado:
            raise ValueError("Estado no encontrado")
        return estado.medir()
