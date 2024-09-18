# nomenclatura versión de paquete: 2.18.1
# 2 = major version (cambios suntanciales que modifican radicalmente la forma como está funcionando actualmente)
# 18 = minor version (nueva funcionalidad en el código, que no suele afectar a lo que ya está)
# 1 = patch (parche para solucionar un optimizar el código)

# ) Mostrar los paquetes que se han instalado con pip.
# >pip list

# ) Desinstalar un paquete
# >pip uninstall requests

# ) Instalar paquete con la ultima versión disponible.
# >pip install requests

# ) Instalar un paquete con una versión en particular.
# >pip install requests==2.18.1

# ) Instalar la ultima versión compatible con la versión 2
# >pip install requests==2.*

# ) Instalar la última versión compatible con la versión 2.18
# >pip install requests==2.18.*

# ) Instalar la versión que más se parezca a lo que se está solicitando
# >pip install requests~=2.18.0

# Por ejemplo, en este caso instaló la versión 2.18.4 el cual era la última versión de requests disponible que se parecía a 2.18.0.

import requests

url = "https://www.google.com"
r = requests.get(url)

print(r)
