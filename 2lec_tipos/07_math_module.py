# import a module
import math

print(round(1.3))  # 1
print(round(1.5))  # 2
print(round(1.7656, 2))  # 1.77
print(abs(-77))  # 77
print(abs(55))  # 55
print(pow(2, 2))  # 4

# using math module

print(math.ceil(1.1))  # 2
print(math.floor(1.999999))  # 1

# valid if the value is not a number
print(math.isnan(23))  # False
print(math.isnan(math.nan))  # True
# print(math.isnan("23"))  # must be real, not str

print(math.pow(10, 3))  # 1000.0
print(math.sqrt(9))  # 3.0
