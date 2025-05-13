import json
from .estado import EstadoCuantico

def guardar_estados(estados_dict, archivo="estados.json"):
    datos = {
        id: {
            "vector": [str(x) for x in estado.vector],
            "base": estado.base
        } for id, estado in estados_dict.items()
    }
    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)

def cargar_estados(archivo="estados.json"):
    estados_cargados = {}
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
        for id, contenido in datos.items():
            vector = [complex(a) for a in contenido["vector"]]
            estados_cargados[id] = EstadoCuantico(id, vector, contenido["base"])
    except FileNotFoundError:
        pass
    return estados_cargados
