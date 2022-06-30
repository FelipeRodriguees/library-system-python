
from book import Book
from user import User
from books import Books

def add_book():
    book = Book("312", "Felipe", 2022, "Test", 21312, "10/01/2022")

    print(book.get_year())
    print(book.set_year(2000))
    print(book.get_year())

    user = User("robertinho.faria", "Robertinho", "Faria", 3725, "Test", "2131321", "teste@teste.com", "2000-18-06")
    print(user.get_postal_code())
    print(user.set_postal_code(None))
    print(user.get_postal_code())

    books = Books(book)
    print(books.add_book(book))
    print(books.get_total())


if __name__ == '__main__':
    add_book()
