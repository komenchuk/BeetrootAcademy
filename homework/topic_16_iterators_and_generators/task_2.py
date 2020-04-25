"""
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function
"""

def in_range(start: int, end: int, step=1):
    if step != 0:
        j = start
        while start < (j + step) <= end:
            yield j
            j += step
    else:
        print('Error!')

for i in in_range(1, 50, 3):
    print(i)