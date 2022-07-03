from book import Book
from books import Books
from user import User
from users import Users

books = Books()
users = Users()
option = 0


def create_book():
    title = input("Digite o título: ")
    author = input("Digite o autor: ")
    year = input("Digite o ano de publicação: ")
    publisher = input("Digite o nome da editora: ")
    number_of_copies_available = input("Digite a número de exemplares disponíveis: ")
    publication_date = input("Digite a data de publicação: ")
    book = {
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "number_of_copies_available": number_of_copies_available,
        "publication_date": publication_date
    }
    return book


def create_user():
    user_name = input("Digite seu nome de usuário: ")
    print(f"Valor salvo: {user_name}")
    name = input("Digite seu nome: ")
    print(f"Valor salvo: {name}")
    last_name = input("Digite seu sobrenome: ")
    print(f"Valor salvo: {last_name}")
    house_number = input("Digite o número da sua casa: ")
    print(f"Valor salvo: {house_number}")
    street = input("Digite o nome da sua rua: ")
    print(f"Valor salvo: {street}")
    postal_code = input("Digite o seu CEP: ")
    print(f"Valor salvo: {postal_code}")
    email = input("Digite o seu email: ")
    print(f"Valor salvo: {email}")
    birth_date = input("Digite a sua data de aniversário: ")
    print(f"Valor salvo: {birth_date}")
    user = {
        "user_name": user_name,
        "name": name,
        "last_name": last_name,
        "house_number": house_number,
        "street": street,
        "postal_code": postal_code,
        "email": email,
        "birth_date": birth_date,
    }
    return user


def start():
    print("+---------------------------+")
    print("| Seja bem vindo a BiblioPy |")
    print("+---------------------------+")

    while True:
        print("+----------------------------+")
        print("+            MENU            +")
        print("+----------------------------+")
        print("Aperte os numerais para seguir")
        print("1 - Para o cadastro de usuário.")
        print("2 - Para para mostrar o usuário completo.")
        print("3 - Para para mostrar a quantidade de usuarios.")
        print("4 - Para o cadastro de livro.")
        print("5 - Para para mostrar todos os livros.")
        print("6 - Para sair")
        option = int(input("Opção: "))

        if option == 1:
            print("Vamos registrar o seu usuário!")
            add_users()
        elif option == 2:
            get_full_user()
        elif option == 3:
            users.get_total()
        elif option == 4:
            print("Vamos cadastrar!")
            add_books()
        elif option == 5:
            get_all_books()
        elif option == 6:
            print("Finalizando...")
            exit()
        else:
            print("Opção inexistente. Tente novamente!")


def add_books():
    qtd_books = int(input("Quantos livros deseja adicionar? "))
    for x in range(qtd_books):
        book_cict = create_book()
        book = Book(book_cict["title"], book_cict["author"], book_cict["year"], book_cict["publisher"],
                    book_cict["number_of_copies_available"], book_cict["publication_date"])
        books.add_book(book)


def add_users():
    qtd_users = int(input("Quantos usuários deseja cadastrar? "))
    for x in range(qtd_users):
        user_cict = create_user()
        print(user_cict)
        user = User(user_cict["user_name"], user_cict["name"], user_cict["last_name"], user_cict["house_number"],
                user_cict["street"], user_cict["postal_code"], user_cict["email"], user_cict["birth_date"])
        users.add_user(user)

def get_all_books():
    books.get_all()

def get_all_users():
    users.get_total()

def get_full_user():
    user_name = input("Digite o nome de usuário: ")
    users.find_user_by_user_name(user_name.title())


if __name__ == '__main__':
    start()
