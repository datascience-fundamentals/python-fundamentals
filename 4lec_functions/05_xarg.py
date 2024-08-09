# example using xargs like *numbers
# *numbers -> It's an iterable so you can loop it
def suma(*numbers):
    res = 0
    for n in numbers:
        res += n
    print(res)


# You can pass the quantity of values you need
suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
