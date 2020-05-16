from random import randint

a = randint(1, 100)
b = randint(1, 100)
Answer = a + b

UserAnswer = int(input(f'{a} + {b} = '))
if UserAnswer == Answer:
    print('True')
else:
    print(f'False! Answer: {Answer}!')
