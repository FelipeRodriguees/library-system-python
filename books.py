class Books:
    def __init__(self):
        self.__list_books = []

    def add_book(self, book):
        self.__list_books.append(book)
        print(len(self.__list_books))

    def get_all(self):
        for book in self.__list_books:
            print("+--------------------------------+")
            print("Título: ", book.title)
            print("Autor: ", book.author)
            print("Ano: ", book.year)
            print("Editora: ", book.publisher)
            print("Número de exemplares: ", book.number_of_copies_available)
            print("Data de publicação: ", book.publication_date)
            print("+--------------------------------+")

    def find_title(self, title):
        for book in self.__list_books:
            if book.title == title:
                print("+--------------------------------+")
                print("Título: ", book.title)
                print("Autor: ", book.author)
                print("Ano: ", book.year)
                print("Número de exemplares: ", book.number_of_copies_available)
                print("+--------------------------------+")
                return book

    def update_title(self, old_title, new_title):
        for book in self.__list_books:
            if book.title == old_title:
                book.set_title(new_title)
                print("Título atualizado!")

    def find_title_for_loan(self, title):
        for book in self.__list_books:
            if book.title == title and book.number_of_copies_available > 0:
                print("+--------------------------------+")
                print("Título: ", book.title)
                print("Autor: ", book.author)
                print("Ano: ", book.year)
                print("Número de exemplares: ", book.number_of_copies_available)
                print("+--------------------------------+")
                book.number_of_copies_available -= 1
                return book

    def find_author(self, author):
        for book in self.__list_books:
            if book.author == author:
                return book

    def update_author(self, title, old_author, new_author):
        for book in self.__list_books:
            if book.title == title and book.author == old_author:
                book.set_set_author(new_author)
                print("Autor atualizado!")

    def find_publisher(self, publisher):
        for book in self.__list_books:
            if book.publisher == publisher:
                return book

    def update_publisher(self, title, old_publisher, new_publisher):
        for book in self.__list_books:
            if book.title == title and book.publisher == old_publisher:
                book.set_publisher(new_publisher)
                print("Editora atualizada!")

    def find_publication_date(self, publication_date):
        for book in self.__list_books:
            if book.publication_date == publication_date:
                return book

    def update_publication_date(self, title, old_publication_date, new_publication_date):
        for book in self.__list_books:
            if book.title == title and book.publication_date == old_publication_date:
                book.set_publication_date(new_publication_date)
                print("Data depublicação atualizada!")

    def update_copies_available(self, title, number_of_copies_available):
        for book in self.__list_books:
            if book.title == title:
                book.set_number_of_copies_available(number_of_copies_available)
                print("Número de exemplares atualizado!")

    def update_year(self, title, year):
        for book in self.__list_books:
            if book.title == title:
                book.set_year(year)
                print("Ano atualizado!")


    def remove_book_from_name(self, title):
        for book in self.__list_books:
            if book.title == title:
                index = self.__list_books.index(book)
                self.__list_books.pop(index)

    def get_total(self):
        return len(self.__list_books)
