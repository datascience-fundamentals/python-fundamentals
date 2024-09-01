from pathlib import Path

path = Path("10lec_routes_directory")
# path.exists()  # If path exists
# path.mkdir() # It creates an directory
# path.rmdir() # It removes directory whereas direcoty is empty
# path.rename("chanchito-feliz")  # it renames the drectory path to the target path
print(path.iterdir())  # It returns an generator object which is iterable
# It searches all elements into the path which matches with pattern
print(path.glob("*.py"))
# It search all element into the path wich matches with pattern recursively
print(path.rglob("*.py"))

archivos = [p for p in path.iterdir() if not p.is_dir()]
# [WindowsPath('10lec_routes_directory/l1_route.py'), WindowsPath('10lec_routes_directory/l2_directory.py')]
print(archivos)
archivos = [p for p in path.glob("l1_*.py")]
print(archivos)  # [WindowsPath('10lec_routes_directory/l1_route.py')]
archivos = [p for p in path.glob("**/*.py")]
# [WindowsPath('10lec_routes_directory/l1_route.py'), WindowsPath('10lec_routes_directory/l2_directory.py'), WindowsPath('10lec_routes_directory/demo/file.py')]
print(archivos)
archivos = [p for p in path.rglob("*.py")]
# [WindowsPath('10lec_routes_directory/l1_route.py'), WindowsPath('10lec_routes_directory/l2_directory.py'), WindowsPath('10lec_routes_directory/demo/file.py')]
print(archivos)
