
import random

class Book:

    def __init__(self, title, author, year, publisher, number_of_copiesa_vailable, publication_date):
        self.__id = random.randint(1, 1000),
        self.__title = title,
        self.__author = author,
        self.__year = year,
        self.__publisher = publisher,
        self.__number_of_copiesa_vailable = number_of_copiesa_vailable,
        self.__publication_date = publication_date

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_year(self, year):
        try:
            self.__year = year
        except ValueError:
            print("This value was no valid number. Try again!")

    def get_year(self):
        return self.__year

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def get_publisher(self):
        return self.__publisher

    def set_number_of_copiesa_vailable(self, number_of_copiesa_vailable):
        try:
            self.__number_of_copiesa_vailable = number_of_copiesa_vailable
        except ValueError:
            print("This value was no valid number. Try again!")

    def get_number_of_copiesa_vailable(self):
        return self.__number_of_copiesa_vailable

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_publication_date(self):
        return self.__publication_date