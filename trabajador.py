import sys
import time

print("Trabajador iniciado")

if len(sys.argv) < 2:
    print(
        "ERROR: no se ha recibido ninguna tarea",
        file=sys.stderr
    )
    sys.exit(2)

tarea = sys.argv[1].lower()

if tarea == "rapida":
    time.sleep(1)
    print("RESULTADO: tarea rápida completada")
    sys.exit(0)

elif tarea == "lenta":
    time.sleep(5)
    print("RESULTADO: tarea lenta completada")
    sys.exit(0)

elif tarea == "error":
    print(
        "ERROR: la tarea no se ha podido procesar",
        file=sys.stderr
    )
    sys.exit(3)

else:
    print(
        f"ERROR: tarea desconocida: {tarea}",
        file=sys.stderr
    )
    sys.exit(4)