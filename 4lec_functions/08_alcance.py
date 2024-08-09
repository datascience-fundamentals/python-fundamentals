# the global variables just can be called and manipulated in the global scope
saludo = "Hola global"
num = 25


def saludar():
    # print(saludo) -> It gives an error, because saludo
    # has not been declared into saludar() yet.
    # It meant that you can not use a variable which has been created
    # outisde the scope or in a higher scope, only in the same scope.

    # saludo is a new variable which is created into saludar() and you can use
    # in saludar()'s scope.
    saludo = "hola mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


def addTwo():
    # you can manipulate a global variable using 'global' keyword
    # but It is a bad practice
    global num
    num += 2


saludar()  # Hola mundo
saludaChanchito()  # Hola Chanchito
print(saludo)  # Hola global

print(num)  # 25
addTwo()
print(num)  # 27
