import random

a = random.randint(1, 100)
b = random.randint(1, 100)
Answer = a + b

print(f'{a} + {b} = ')
UserAnswer = int(input(' '))
if UserAnswer == Answer:
    print('True')
else:
    print(f'False! Answer: {Answer}!')