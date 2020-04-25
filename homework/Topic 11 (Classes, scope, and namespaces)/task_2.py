"""
Doggy age

Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age. Then create a method `human_age`
which returns the dog’s age in human equivalent.
"""


class Dog:

    def __init__(self, dog_age):
        self.age_factor = 7
        self.age = dog_age

    def human_age(self):
        human_age = self.age_factor * self.age
        print(f'If dog age = {self.age}, human age = {human_age}')
        return human_age


dog = Dog(7)
dog.human_age()
