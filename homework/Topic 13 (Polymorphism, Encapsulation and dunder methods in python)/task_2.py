"""Library

Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class

Methods:
- new_book(name: str, year: int, author: Author) -
returns an instance of Book class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books"""


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(name: str, year: int, author: Author.object):
        pass

    def group_by_author(author: Author.object):
        pass

    def group_by_year(year: int):
        pass

class Book:
    def __init__(self, name: str, year: int, author: Author.object):
        self.name = name
        self.year = year
        self.author = author


class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
