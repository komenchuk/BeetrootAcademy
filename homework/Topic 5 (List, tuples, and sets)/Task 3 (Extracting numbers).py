import random

a = []

for x in range (1, 100):
    if (x % 7 == 0) and (x % 5 != 0):
        a.append(str(x))

print(', '.join(a))