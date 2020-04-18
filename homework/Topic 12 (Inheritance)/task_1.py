"""School

Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher. """


class Person:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def info(self):
        information = f"Hello, my name is {self.name}. I'm {self.age} years old."
        print(information)


class Teacher(Person):
    def __init__(self, name, age, school, specialty, salary):
        super().__init__(name, age, school)
        self.specialty = specialty
        self.salary = salary

    def info(self):
        information = f"My name is {self.name}. I'm {self.age} years old. My specialty is {self.specialty}. My salary: {self.salary} UAH/mounth."
        print(information)


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age, school)

    def info(self):
        information = f"My name is {self.name}. I'm {self.age} years old. I'm student of the school number {self.school}."
        print(information)


test = Student('Oleg', 15, 7)
test.info()
