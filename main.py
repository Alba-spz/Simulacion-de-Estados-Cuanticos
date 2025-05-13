from simulador_cuantico.repositorio import RepositorioDeEstados
from simulador_cuantico.operador import OperadorCuantico

repo = RepositorioDeEstados()

# Agregar estado psi = |+> = [0.707, 0.707]
repo.agregar_estado("psi", [0.707, 0.707], "computacional")

# Definir puerta Hadamard
H = OperadorCuantico("H", [[0.707, 0.707], [0.707, -0.707]])

# Aplicar H a psi (debería volver a |0>)
repo.aplicar_operador("psi", H, "psi_H")

# Mostrar resultado
estado_resultado = repo.obtener_estado("psi_H")
if estado_resultado:
    print("\nEstado psi_H:")
    print(estado_resultado)
    print("Vector:", estado_resultado.vector)

# Confirmar que los estados están bien en el repositorio
print("\n>>> Todos los estados:")
for desc in repo.listar_estados():
    print(desc)


