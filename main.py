from simulador_cuantico.estado import EstadoCuantico
from simulador_cuantico.operador import OperadorCuantico

estado = EstadoCuantico("q0", [1, 0], "computacional")  # |0⟩
opX = OperadorCuantico("X", [[0, 1], [1, 0]])            # Puerta X

nuevo_estado = opX.aplicar(estado)

print(nuevo_estado)             # Esperado: q0_X: vector=[0.+0.j, 1.+0.j] en base computacional
print(nuevo_estado.vector)      # Esperado: [0.+0.j, 1.+0.j]
print(nuevo_estado.medir())     # Esperado: {'0': 0.0, '1': 1.0}
