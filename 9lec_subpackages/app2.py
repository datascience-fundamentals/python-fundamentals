# dir() -> It lists all subpackages found in a specific package
import users
import users.manage

# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'actions', 'manage', 'taxes']
print(dir(users))
print(users.__name__)  # users
print(users.__package__)  # users
# ['c:\\python-fundamentals\\9lec_subpackages\\users']
print(users.__path__)
# c:\python-fundamentals\9lec_subpackages\users\__init__.py
print(users.__file__)

print(users.manage.__name__)  # users.manage
print(users.manage.__package__)  # users.manage
# ['c:\\python-fundamentals\\9lec_subpackages\\users\\manage']
print(users.manage.__path__)
# d:\python-fundamentals\9lec_subpackages\users\manage\__init__.py
print(users.manage.__file__)
