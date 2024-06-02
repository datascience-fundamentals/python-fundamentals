# and, or, not

gas = False
encendido = True
edad = 18

if gas and encendido:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")

if gas or encendido:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")

if not gas and encendido:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")

# 'and' has higher precedence than the logic operator 'or'
# True or False and False is equivalent to True or (False and False)

if not gas and (encendido or edad > 17):
    print("Puedes avanzar")
else:
    print("No puedes avanzar")
