"""Write a Python program to access a function inside a function
(Tips: use function, which returns another function)"""


# Create class
class Kilometers:
    def __init__(self, kilometers):
        self.miles = 1.609
        self.kilometers = kilometers

    def miles_to_kilometers(self):
        miles_to_kilometers = self.miles * self.kilometers
        print(f'In {self.kilometers} kilometers - {miles_to_kilometers} miles.')
        return miles_to_kilometers


# Create information for the class
kilometers_1 = Kilometers(100)
kilometers_1.miles_to_kilometers()
