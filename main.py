from simulador_cuantico.repositorio import RepositorioDeEstados

repo = RepositorioDeEstados()

# Listar estados vacíos
print(">>> Estados actuales:")
for linea in repo.listar_estados():
    print(linea)

# Agregar algunos estados
repo.agregar_estado("q0", [1, 0], "computacional")
repo.agregar_estado("q1", [0, 1], "computacional")

print("\n>>> Después de agregar q0 y q1:")
for linea in repo.listar_estados():
    print(linea)

# Intentar agregar un duplicado
repo.agregar_estado("q1", [0.5, 0.5], "computacional")

# Obtener estado existente
estado_q0 = repo.obtener_estado("q0")
print(f"\nMedición de q0: {estado_q0.medir()}" if estado_q0 else "Estado q0 no encontrado.")

# Eliminar un estado
repo.eliminar_estado("q1")

print("\n>>> Después de eliminar q1:")
for linea in repo.listar_estados():
    print(linea)

