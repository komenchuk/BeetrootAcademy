import random

# First version
a = random.randint(1,10)

dict = {a:a**2}

print(dict)

# Second version
dict_2 = {b:b**2 for b in random.sample(range(10), 5)}

print(dict_2)

# Third version
dict_3 = {c:c**2 for c in range(1, 10)}

print(dict_3)