# Прибавление
def add (x, y):
    return x + y

# Вычитание
def subtract (x, y):
    return x - y

# Умножение
def multiply (x, y):
    return x * y

# Деление
def divide (x, y):
    return x / y

print("Select operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

# Выбор операции и чисел
choice = input("Enter your choice (1/2/3/4) --> ")

num1 = float(input("Enter first number --> "))
num2 = float(input("Enter second number --> "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    try:
        num1 / 0
    except ZeroDivisionError:
        print("Division by 0!")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalide input!")