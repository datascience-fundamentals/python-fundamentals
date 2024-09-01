from pathlib import Path
from zipfile import ZipFile

with ZipFile("files/compressed.zip", "w") as zip:
    archivos = [archivo for archivo in Path().rglob(
        "*.*") if r"files\compressed.zip" != str(archivo)]
    for archivo in archivos:
        zip.write(archivo)
