from datetime import datetime


class Books:
    def __init__(self):
        self.__list_books = []

    def serializer(self, book):
        __book = {
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "publisher": book.publisher,
            "number_of_copies_available": book.number_of_copies_available,
            "publication_date": book.publication_date
        }
        return __book

    def add_book(self, book):
        print(self.serializer(book))
        self.__list_books.append(self.serializer(book))
        print(len(self.__list_books))

    def get_all(self):
        for book in self.__list_books:
            print("+--------------------------------+")
            print("Título: ", book["title"])
            print("Autor: ", book["author"])
            print("Ano: ", book["year"])
            print("Editora: ", book["publisher"])
            print("Número de exemplares: ", book["number_of_copies_available"])
            print("Data de publicação: ", book["publication_date"])
            print("+--------------------------------+")

    def find_title(self, title):
        for book in self.__list_books:
            if book["title"] == title:
                print("+--------------------------------+")
                print("Título: ", book["title"])
                print("Autor: ", book["author"])
                print("Ano: ", book["year"])
                print("Número de exemplares: ", book["number_of_copies_available"])
                print("+--------------------------------+")
                return book

    def find_title_for_loan(self, title):
        for book in self.__list_books:
            if book["title"] == title and book["number_of_copies_available"] > 0:
                print("+--------------------------------+")
                print("Título: ", book["title"])
                print("Autor: ", book["author"])
                print("Ano: ", book["year"])
                print("Número de exemplares: ", book["number_of_copies_available"])
                print("+--------------------------------+")
                book["number_of_copies_available"] -= 1
                return book

    def find_author(self, author):
        for book in self.__list_books:
            if book.author == author:
                return book

    def find_publisher(self, publisher):
        for book in self.__list_books:
            if book.publisher == publisher:
                return book

    def find_publication_date(self, publication_date):
        for book in self.__list_books:
            if book.publication_date == publication_date:
                return book

    def remove_book_from_name(self, title):
        for book in self.__list_books:
            if book.title == title:
                index = self.__list_books.index(book)
                self.__list_books.pop(index)

    def get_total(self):
        return len(self.__list_books)
