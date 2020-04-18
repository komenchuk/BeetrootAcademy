"""Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

    square_nums (takes a list of integers and returns the list of squares)
    remove_positives (takes a list of integers and returns it without positive numbers
    filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
"""

import calendar


class Mathematician:

    @staticmethod
    def square_nums(arg):
        return list(map(lambda x: x ** 2, arg))

    @staticmethod
    def remove_positives(arg):
        return list(map(lambda x: x < 0, arg))

    @staticmethod
    def filter_leaps(arg):
        return list(filter(calendar.isleap, arg))


a = Mathematician()
print(a.square_nums([7, 11, 5, 4]))
print(a.remove_positives([26, -11, -8, 13, -90]))
print(a.filter_leaps([2001, 1884, 1995, 2003, 2020]))
