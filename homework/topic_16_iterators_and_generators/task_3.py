"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""

class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]


my_str = 'Komenchuk'
for elem in MyIterable(my_str):
    print(elem, end='')
print()