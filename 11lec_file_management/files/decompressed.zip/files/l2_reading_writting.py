
from pathlib import Path
archivo = Path("files/file-test.txt")

# read_text() -> It allows you to readthe file content
file_content = archivo.read_text("utf-8")
textos = file_content.split("\n")
print(textos)

textos.insert(0, "Hola mundo")
# write_text() -> It replace the file content with a new one
archivo.write_text("\n".join(textos), "utf-8")
