from datetime import datetime, timedelta

fecha = datetime(2023, 1, 1, 10, 10, 10)
# timedelta allows you to increase or decrease an specific part of the time
fecha2 = datetime(2023, 2, 1, 10, 10, 10) + timedelta(minutes=10)

# when you substract two datetimes, It returns a vlaue with timedelta type
delta = fecha2 - fecha
print(delta)  # 31 days, 0:10:00
print("dias", delta.days)  # 31 (days's difference)
print("segundos", delta.seconds)  # 600 (seconds's difference)
print("microsegundos", delta.microseconds)  # 0 (microseconds' difference)
# 2679000.0 (total second's difference)
print("total_seconds()", delta.total_seconds())
