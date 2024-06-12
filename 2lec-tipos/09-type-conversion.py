# int() -> convert value to int
n1 = int("24")
n2 = int(24.7)
print(n1)  # 24
print(n2)  # 24

# float() -> convert value to float
n1 = float("24.7")
n2 = float(24.7)
print(n1)  # 24.7
print(n2)  # 24.7

# str() -> convert value to string
str1 = str(24.7)
print(str1)  # 124

# bool() -> convert value to boolean
print(bool(""))  # False
print(bool(0))  # False
print(bool([]))  # False
print(bool(None))  # false
print(bool("0"))  # True
print(bool(" "))  # True
print(bool(24))  # True
print(bool([1]))  # True

# list() -> convert value to list
print(list("hola"))  # -> ['h','o','l','a']
print(list(range(1, 3)))  # -> [1, 2]
