
class Books:
    def __init__(self, book):
        self.__book = book
        self.list_books = [self.__book]

    def add_book(self, book):
        self.list_books.append(book)

    def find_title(self, list_books, title):
        for book in list_books:
            if book.title == title:
                return book

    def find_author(self, list_books, author):

        for book in list_books:
            if book.author == author:
                return book

    def find_publisher(self, list_books, publisher):
        for book in list_books:
            if book.publisher == publisher:
                return book

    def find_publication_date(self, list_books, publication_date):
        for book in list_books:
            if book.publication_date == publication_date:
                return book

    def remove_book_from_name(self, list_books, title):
        for book in list_books:
            if book.title == title:
                index = list_books.index(book)
                list_books.pop(index)

    def get_total(self):
        return len(self.list_books)
