"""Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0.
Tips: see the documentation for the enumerate function"""


def with_index(iterable, start=0):
    i = start
    for n in iterable:
        yield i, n
        i += 1


dict = {'a': 1, 'b': 2, 'c': 3}
for j in with_index(dict):
    print(j, type(j))
