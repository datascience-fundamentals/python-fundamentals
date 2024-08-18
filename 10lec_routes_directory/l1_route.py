# Raw String (r"") -> It doesn't take escape character backslash
from pathlib import Path

# It represent's an absolute route in windows
# Path(r"C:\Archivos de Programa\Minecraft")
# Path("/usr/bin")  # It represent's an absolute route in linux
# Path()  # It references the routes's value where the program is executed
# Path.home()  # It references the home route where the program is executed
# Path("one/__init__.py")  # It represent's a realtive route
path = Path("hola_mundo/mi_archivo.py")
path.is_file()  # If It is an file
path.is_dir()  # If It is an directory
path.exists()  # It path exists

print(
    path.name,  # mi_archivo.py -> filename with its extension
    path.stem,  # mi_archivo -> filename without its extension
    path.suffix,  # .py -> file's extension
    path.parent,  # hola_mundo -> file's parent directory
    path.absolute()  # d:\python\hola_mundo\mi_archivo.py -> absolute route
)

# It changes the filename and its extension
p = path.with_name("chanchito.txt")
print(p)  # hola_mundo/chanchito.txt
p = path.with_suffix(".bat")
print(p)  # hola_mundo/mi_archivo.bat
p = path.with_stem("feliz")  # It changes only the filename
print(p)  # hola_mundo/feliz.py
