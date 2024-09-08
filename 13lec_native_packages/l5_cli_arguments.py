from pathlib import Path
import sys
import os

print(sys.argv)  # It list all argument you pass when you execute the python program


def cli(args):
    if 1 == len(args):
        print("no se pasaron argumentos")
        return
    if 3 != len(args):
        print("se necesitan 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("origen no existe")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("El destino no debe existir")
        return

    os.rename(str(origen), str(destino))
    print("El archivo fue renombrado con exito")


cli(sys.argv)
