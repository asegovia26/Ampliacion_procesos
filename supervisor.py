import subprocess
import sys
from pathlib import Path


script_trabajador = Path(__file__).with_name(
    "trabajador.py"
)

# 1. Solicitud y normalización de la entrada del usuario
modo = input(
    "Introduce una tarea: rapida, lenta o error: "
).strip().lower()

# 2. Validación previa en el proceso padre mediante un conjunto (O(1))
tareas_validas = {
    "rapida",
    "lenta",
    "error"
}

if modo not in tareas_validas:
    print("La tarea indicada no es válida.")
    sys.exit(1)

# 3. Ejecución del proceso hijo con captura de salidas
resultado = subprocess.run(
    [
        sys.executable,
        str(script_trabajador),
        modo
    ],
    capture_output=True,
    text=True
)

# 4. Presentación de resultados y flujos de salida
print("Código de retorno:", resultado.returncode)
print("Salida normal:")
print(resultado.stdout)

print("Salida de error:")
print(resultado.stderr)