"""Write a function that takes in two numbers from the user via input(),
call the numbers a and b, and then returns the value of squared a divided by b,
construct a try-except block which raises an exception if the two values given by the input function were not numbers,
and if value b was zero (cannot divide by zero)."""


def operation():
    a = float(input("Enter first number --> "))
    b = float(input("Enter second number --> "))
    result = a ** 2 / b
    print(result)
    return result


try:
    operation()
except (ZeroDivisionError, ValueError) as error:
    print(f'Error: {error}')
