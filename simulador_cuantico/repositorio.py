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

    def aplicar_operador(self, id_estado: str, operador, nuevo_id: str = None):
        estado_original = self.obtener_estado(id_estado)
        if estado_original is None:
            print(f"Error: no se encontró el estado con id '{id_estado}'")
            return

        # Validación de dimensiones
        n = len(estado_original.vector)
        if len(operador.matriz) != n or any(len(fila) != n for fila in operador.matriz):
            print(f"Error: la dimensión del operador '{operador.nombre}' no coincide con la del estado '{id_estado}'")
            return

        # Aplicar el operador
        nuevo_estado = operador.aplicar(estado_original)

        # Asignar id nuevo (o derivado automáticamente)
        if nuevo_id is not None:
            nuevo_estado.id = nuevo_id
        else:
            nuevo_estado.id = f"{id_estado}_{operador.nombre}"

        # Almacenar: permitir sobreescritura si el id ya existe
        self.estados[nuevo_estado.id] = nuevo_estado

    def medir_estado(self, id_estado: str):
        estado = self.obtener_estado(id_estado)
        if estado is None:
            print(f"Error: no se encontró el estado con id '{id_estado}'")
            return

        probabilidades = estado.medir()
        print(f"Medición del estado '{id_estado}' (base {estado.base}):")
        for i, p in enumerate(probabilidades):
            porcentaje = round(p * 100, 2)
            print(f"  - Estado base {i}: {porcentaje}%")
