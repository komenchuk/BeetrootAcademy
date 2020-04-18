"""
Write a Python program to detect the number of local variables declared in a function.
"""


# Create class
class Human:
    def __init__(self, name, age, country, city):
        self.name = name
        self.age = age
        self.country = country
        self.city = city

    def info(self):
        print(
            f'Hello everyone, my name is {self.name}, I\'m {self.age} years old, I live in {self.country} {self.city} city.')


# Create information for the class
human_1 = Human('Oleh', 22, 'Ukraine', 'Vinnytsia')
human_1.info()
