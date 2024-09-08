# import time

# print(time.time())  # It returns a UTC timestamp value (1725348359.007392)

from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)
fecha3 = datetime(2023, 1, 1)
ahora = datetime.now()

print(fecha)  # 2023-01-01 00:00:00
print(ahora)  # 2024-09-03 02:28:47.699042

# It allows you to convert string to date
fechaFromStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechaFromStr)  # 2023-01-03 00:00:00

# It allows you to convert date to string
fechaStrFromDate = fechaFromStr.strftime("%Y.%m.%d")
print(fechaStrFromDate)  # 2023.01.03

# comparing dates
print(fecha == fecha3)  # True
print(fecha > fecha2)  # False

print(
    fecha.year,  # 2023
    fecha.month,  # 1
    fecha.day,  # 1
    fecha.hour,  # 0
    fecha.minute,  # 0
    fecha.second,  # 0
)
