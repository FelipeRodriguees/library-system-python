from datetime import datetime

class Borrowed:

    def __init__(self):
        self.__borrowed = []

    def serializer(self, book, user_name, date_give_back):
        __book = {
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "publisher": book.publisher,
            "number_of_copies_available": book.number_of_copies_available,
            "publication_date": book.publication_date,
            "user_name": user_name,
            "loan_date": datetime.today().strftime('%Y-%m-%d'),
            "date_give_back": date_give_back,
        }
        return __book

    def add_borrowed(self, book, user_name, date_give_back):
        self.__borrowed.append(self.serializer(book, user_name, date_give_back))
        print("Livro salvo com sucesso!")
        return self.serializer(book, user_name, date_give_back)

    def get_all_borrowed(self):
        for borrowed in self.__borrowed:
            print("+--------------------------------+")
            print("Título: ", borrowed["title"])
            print("Autor: ", borrowed["author"])
            print("Data de  emprestimo: ", borrowed["loan_date"])
            print("Data de devolucao: ", borrowed["date_give_back"])
            print("Usuário responsável: ", borrowed["user_name"])
            print("+--------------------------------+")

    def return_book(self, user_name, title):
        for i, borrowed in self.__borrowed:
            if borrowed.user_name == user_name:
                print("Livro Devolvido")
                return borrowed

    def delete_book(self, borr):
        print(borr)
        # self.__borrowed.pop(borr)

    def get_qunatity(self):
        print("A quantidade de livros emprestados é ", len(self.__borrowed))
