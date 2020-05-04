"""
Write a Python program to detect the number of local variables declared in a function.
"""


# Create class
class Human:
    def __init__(self, name, age, country, city):
        self.name = name.title()
        self.age = int(age)
        self.country = country.title()
        self.city = city.title()

    def info(self):
        print(
            f'Hello everyone, my name is {self.name}, I\'m {self.age} years old, I live in {self.country} {self.city} city.')


# Create information for the class
human_1 = Human('oleh', 22, 'ukraine', 'vinnytsia')
human_1.info()
