from simulador_cuantico.repositorio import RepositorioDeEstados
from simulador_cuantico.operador import OperadorCuantico

repo = RepositorioDeEstados()

# Estado |0⟩
repo.agregar_estado("q0", [1, 0], "computacional")
repo.medir_estado("q0")
# Esperado: 100% estado 0, 0% estado 1

# Estado |+⟩
repo.agregar_estado("plus", [0.707, 0.707], "computacional")
repo.medir_estado("plus")
# Esperado: ~50% en cada base

# Estado no existente
repo.medir_estado("no_existe")  # Debería mostrar error


