# QUEUE is FIFO (First In First Out)

from collections import deque

fila = deque([1, 2])

# to add elements in the queue
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)

# to delete the first element from the queue
primerElemento = fila.popleft()
print(primerElemento)  # 1
print(fila)  # [2,3,4,5]

# getting the first element from the queue
print(fila[0])  # 2
