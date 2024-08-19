from pathlib import Path
import db
import graphql
import api

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]
dependencies = {
    "db": db,
    "api": graphql,
    "graphql": api,
}


def load(p):
    paquete = __import__(str(p.name).replace("/", "."))
    try:
        paquete.init(**dependencies)
    except Exception as ex:
        print(f"el paquete no tiene funcion init")
        print(ex)


list(map(load, paths))
