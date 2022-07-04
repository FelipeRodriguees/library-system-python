import random


class Book:

    def __init__(self, title, author, year, publisher, number_of_copies_available, publication_date):
        self.__id = random.randint(1, 1000)
        self.__title = title
        self.__author = author
        self.__year = year
        self.__publisher = publisher
        self.__number_of_copies_available = number_of_copies_available
        self.__publication_date = publication_date

    @property
    def title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    def set_set_author(self, author):
        self.__author = author

    @property
    def year(self):
        return self.__year

    def set_year(self, year):
        try:
            self.__year = year
        except ValueError:
            print("This value was no valid number. Try again!")

    @property
    def publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher

    @property
    def number_of_copies_available(self):
        return self.__number_of_copies_available

    def set_number_of_copies_available(self, number_of_copies_available):
        try:
            self.__number_of_copies_available = number_of_copies_available
        except ValueError:
            print("This value was no valid number. Try again!")

    @property
    def publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date
