# example using keyword arguments
def get_product(**datos):
    print(datos["id"], datos["name"])


# you always must include a key and value as argument
# in case the function receive keyword arguments.
# You can the quatity of pair(key-value) you need
get_product(id=23,
            name="iPhone",
            desc="Esto es un iphone")
