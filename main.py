
from book import Book
from user import User
from books import Books

def add_book():
    book = Book("312", "felipe", 2022, "Test", 21312, "10/01/2022")
    book2 = Book("Jordel", "felipe", 2022, "Test", 21312, "10/01/2022")

    user = User("robertinho.faria", "Robertinho", "Faria", 3725, "Test", "2131321", "teste@teste.com", "2000-18-06")

    books = Books(book)
    books.add_book(book2)
    print("Livros adicionados")


    books.lend_book("Jordel", user)
    print(user.borrowing)
    print(books.get_all())
    print(user.borrowing)


    # O usuario deve poder alugar um livro, este

if __name__ == '__main__':
    add_book()
