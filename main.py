from book import Book
from books import Books
from user import User
from users import Users
from borrowed import Borrowed

books = Books()
users = Users()
borrowed = Borrowed()
option = 0


def create_book():
    title = input("Digite o título: ")
    author = input("Digite o autor: ")
    year = int(input("Digite o ano de publicação: "))
    publisher = input("Digite o nome da editora: ")
    number_of_copies_available = int(input("Digite a número de exemplares disponíveis: "))
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
    house_number = int(input("Digite o número da sua casa: "))
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
        print("6 - Para emprestar um livro.")
        print("7 - Para ver todos livros emprestados.")
        print("8 - Para buscar um livro pelo titulo.")
        print("9 - Total de livros registrados.")
        print("10 - Para devolver um livro.")
        print("11 - Atualizar o título do livro.")
        print("12 - Atualizar o autor do livro.")
        print("13 - Atualizar a editora do livro.")
        print("14 - Atualizar a data de publicação do livro.")
        print("15 - Alterar exemplares do livro.")
        print("16 - Alterar o ano do livro.")

        print("17 - Alterar o nome de usuário.")
        print("18 - Alterar o nome do usuário.")
        print("19 - Alterar o sobrenome do usuário.")
        print("20 - Alterar o número da casa do usuário.")
        print("21 - Alterar a rua do usuário.")
        print("22 - Alterar o CEP.")
        print("23 - Alterar o email do usuário.")
        print("24 - Alterar a data de aniversário do usuário.")
        print("25 - Para sair.")
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
            new_loan()
        elif option == 7:
            get_all_borrowed()
        elif option == 8:
            get_book_by_title()
        elif option == 9:
            get_total_books()
        elif option == 10:
            return_book()
        elif option == 11:
            update_book_title()
        elif option == 12:
            update_book_author()
        elif option == 13:
            update_book_publisher()
        elif option == 14:
            update_book_publication_date()
        elif option == 15:
            update_copies_available()
        elif option == 16:
            update_book_year()
        elif option == 17:
            update_user_name()
        elif option == 18:
            update_name()
        elif option == 19:
            update_last_name()
        elif option == 20:
            update_house_number()
        elif option == 21:
            update_street()
        elif option == 22:
            update_postal_code()
        elif option == 23:
            update_email()
        elif option == 24:
            update_birth_date()
        elif option == 25:
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


def get_book_by_title():
    book_name = input("Digite o nome do livro: ")
    books.find_title(book_name)


def get_all_users():
    users.get_total()


def get_full_user():
    user_name = input("Digite o nome de usuário: ")
    users.find_user_by_user_name_and_print(user_name)


def new_loan():
    user_name = input("Digite o nome de usuário: ")
    user = users.find_user_by_user_name(user_name)
    book_name = input("Digite o nome do livro: ")
    book = books.find_title(book_name)
    date_give_back = input("Digite a data de devolução [yyyy-mm-dd]: ")
    borrowed.add_borrowed(book, user["user_name"], date_give_back)


def get_all_borrowed():
    borrowed.get_all_borrowed()


def get_total_books():
    total = books.get_total()
    print("O total de livros é ", total)


def return_book():
    user_name = input("Digite o nome de usuário: ")
    title = input("Digite o nome do livro: ")
    borr = borrowed.return_book(user_name, title)
    borrowed.delete_book(borr)


def update_book_title():
    old_title = input("Digite o título do livro que deseja alterar: ")
    new_title = input("Digite o novo titulo: ")
    books.update_title(old_title, new_title)


def update_book_author():
    title = input("Digite o título do livro: ")
    old_author = input("Digite o nome do autor que deseja alterar: ")
    new_author = input("Digite nome do novo autor: ")
    books.update_author(title, old_author, new_author)


def update_book_publisher():
    title = input("Digite o título do livro: ")
    old_publisher = input("Digite o nome da editora que deseja alterar: ")
    new_publisher = input("Digite nome da nova editora: ")
    books.update_publisher(title, old_publisher, new_publisher)


def update_book_publication_date():
    title = input("Digite o título do livro: ")
    old_publication_date = input("Digite a data de publicação que deseja alterar: ")
    new_publication_date = input("Digite a nova data de publicação: ")
    books.update_publication_date(title, old_publication_date, new_publication_date)


def update_copies_available():
    title = input("Digite o título do livro: ")
    number_of_copies_available = int(input("Digite a quantidade de exemplares que deseja adicionar: "))
    books.update_copies_available(title, number_of_copies_available)


def update_book_year():
    title = input("Digite o título do livro: ")
    year = int(input("Digite o novo ano do livro: "))
    books.update_year(title, year)


def update_user_name():
    old_user_name = input("Digite o nome de usuário antigo: ")
    new_user_name = input("Digite novo o nome de usuário: ")
    users.update_user_name(old_user_name, new_user_name)


def update_name():
    user_name = input("Digite o nome de usuário: ")
    new_name = input("Digite o novo nome: ")
    users.update_name(user_name, new_name)


def update_last_name():
    user_name = input("Digite o nome de usuário: ")
    new_last_name = input("Digite o novo sobrenome: ")
    users.update_last_name(user_name, new_last_name)


def update_house_number():
    user_name = input("Digite o nome de usuário: ")
    new_house_number = int(input("Digite o novo número: "))
    users.update_house_number(user_name, new_house_number)


def update_street():
    user_name = input("Digite o nome de usuário: ")
    new_street = input("Digite o novo endereço: ")
    users.update_street(user_name, new_street)


def update_postal_code():
    user_name = input("Digite o nome de usuário: ")
    new_postal_code = input("Digite o novo CEP: ")
    users.update_postal_code(user_name, new_postal_code)

def update_email():
    user_name = input("Digite o nome de usuário: ")
    new_email = input("Digite o novo email: ")
    users.update_email(user_name, new_email)

def update_birth_date():
    user_name = input("Digite o nome de usuário: ")
    birth_date = input("Digite a nova data de aniversário: ")
    users.update_birth_date(user_name, birth_date)

if __name__ == '__main__':
    start()
