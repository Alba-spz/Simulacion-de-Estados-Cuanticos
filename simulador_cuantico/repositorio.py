from simulador_cuantico.estado import EstadoCuantico

class RepositorioDeEstados:
    def __init__(self):
        self.estados = {}

    def listar_estados(self):
        if not self.estados:
            return ["No hay estados registrados."]
        return [str(estado) for estado in self.estados.values()]

    def agregar_estado(self, id: str, vector, base: str):
        if id in self.estados:
            print(f"Error: ya existe un estado con identificador '{id}'")
            return

        try:
            nuevo_estado = EstadoCuantico(id, vector, base)
            self.estados[id] = nuevo_estado
        except Exception as e:
            print(f"Error al crear el estado cuántico: {e}")

    def obtener_estado(self, id: str):
        return self.estados.get(id, None)

    def eliminar_estado(self, id: str):
        if id in self.estados:
            del self.estados[id]
            print(f"Estado '{id}' eliminado.")
        else:
            print(f"No existe un estado con id '{id}'.")

