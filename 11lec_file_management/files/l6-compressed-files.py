from pathlib import Path
from zipfile import ZipFile

# writing into zip file
# with ZipFile("files/compressed.zip", "w") as zip:
#     archivos = [archivo for archivo in Path().rglob(
#         "*.*") if r"files\compressed.zip" != str(archivo)]
#     for archivo in archivos:
#         zip.write(archivo)  # It allows you to save a file into the zip file

# reading from zip file
with ZipFile("files/compressed.zip", "r") as zip:
    # It allows you to name the files which has been compressed
    nombre_archivos = zip.namelist()
    print(nombre_archivos)
    # It allows you to get info of compressed file
    # such as file_size, compress_size
    info = zip.getinfo("files/l6-compressed-files.py")
    print(info.file_size, info.compress_size)
    # It allows you to extract all files which has been compressed previously
    zip.extractall("files/decompressed.zip")
