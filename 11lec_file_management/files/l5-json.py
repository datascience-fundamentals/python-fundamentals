import json
from pathlib import Path

# writing into file json
# products = [
#     {"id": 1, "name": "Sufboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(products) # it allows you convert python value to string json value
# print(type(data))

# archivo = Path("files/products.json")
# archivo.write_text(data, encoding="utf-8")

# reading from json file
archivo = Path("files/products.json")
data = archivo.read_text(encoding="utf-8")
# It allows you to convert string json value to python value
products = json.loads(data)
print(products)

# updating json file content
products[0]["name"] = "Chanchito Feliz"
data_updated = json.dumps(products)
archivo.write_text(data_updated, encoding="utf-8")
