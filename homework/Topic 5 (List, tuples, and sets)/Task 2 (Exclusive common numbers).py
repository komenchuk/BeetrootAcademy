import random

a = random.sample(range(10), 5)
b = random.sample(range(10), 5)
c = []

for i in a:
    if i in b and i not in c:
        c.append([i])

print(a, b, c)
