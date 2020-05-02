import random

print('Welcome to The Guessing Game')
gamer_attempt = 0

s = int(random.uniform(1, 10))
while gamer_attempt < 6:

    print('What do you think, what number?')
    point = int(input('I think this number is: '))

    gamer_attempt = gamer_attempt + 1

    if point < s:
        print('The number is bigger!')

    if point > s:
        print('The number is less!')

    if point == s:
        break

if point == s:
    gamer_attempt = str(gamer_attempt)
    print('You guessed the number!')

if point != s:
    s = str(s)
    print('Sorry, the attempts are over!')