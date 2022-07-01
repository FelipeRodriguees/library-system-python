
import random

class Book:

    def __init__(self, title, author, year, publisher, number_of_copies_available, publication_date):
        self.__id = random.randint(1, 1000)
        self.__title = title.title()
        self.__author = author.title()
        self.__year = year
        self.__publisher = publisher.title()
        self.__number_of_copies_available = number_of_copies_available
        self.__publication_date = publication_date

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title.title()

    @property
    def author(self):
        return self.__author

    @author.setter
    def set_author(self, author):
        self.__author = author.title()

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        try:
            self.__year = year
        except ValueError:
            print("This value was no valid number. Try again!")

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher.title()

    @property
    def number_of_copies_available(self):
        return self.__number_of_copies_available

    @number_of_copies_available.setter
    def number_of_copies_available(self, number_of_copies_available):
        try:
            self.__number_of_copies_available = number_of_copies_available
        except ValueError:
            print("This value was no valid number. Try again!")

    @property
    def publication_date(self):
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        self.__publication_date = publication_date
