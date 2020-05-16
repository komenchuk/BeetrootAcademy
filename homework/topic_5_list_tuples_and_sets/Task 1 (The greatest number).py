from random import randint

lst = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = randint(1, 100)
    lst.append(numbers)

print(f'{lst}\nMaximum element in the list is : {max(lst)}')
