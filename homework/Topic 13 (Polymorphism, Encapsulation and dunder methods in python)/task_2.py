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

from typing import List, Any


class Author:

    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author('{self.name}, {self.country}, {self.birthday}')."

    def __str__(self):
        return f"Author {self.name} was born in {self.country} in {self.birthday}."


class Library:

    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        self.books.append(Book(name, year, author))

    def group_by_author(self, author: Author):
        list_by_author = list(filter(lambda x: x.author is author, self.books))
        return list_by_author

    def group_by_year(self, year: int):
        list_by_year: List[Any] = list(filter(lambda x: x.year is year, self.books))
        return list_by_year

    def __repr__(self):
        return f'Library('
        {self.name}
        ')\n'

    def __str__(self):
        list_of_books = ''.join(map(lambda x: f'{x.author.name}, {x.name}, {x.year}', self.books))
        return list_of_books


class Book:
    all_books = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.all_books += 1

    def __del__(self):
        Book.all_books -= 1

    def __repr__(self):
        return f'Book('
        {self.name}, {self.year}, {self.author}
        ')'

    def __str__(self):
        return f'The book {self.name} was written in {self.year} by {self.author}'


author_1 = Author('Arthur Conan Doyle', 'United Kingdom', '22 May 1859')

library_1 = Library('The British Library')
library_1.new_book('The Adventures of Sherlock Holmes', 1892, author_1)

print(library_1)
print(Book.all_books)
