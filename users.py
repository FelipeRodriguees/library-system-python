class Users:
    def __init__(self):
        self.__list_users = []

    def update_user_name(self, old_user_name, new_user_name):
        for user in self.__list_users:
            if user.user_name == old_user_name:
                user.set_user_name(new_user_name)
                print("Atuallização realizada!")

    def update_name(self, user_name, new_name):
        for user in self.__list_users:
            if user.user_name == user_name:
                user.set_name(new_name)
                print("Atuallização realizada!")

    def update_last_name(self, user_name, new_last_name):
        for user in self.__list_users:
            if user.user_name == user_name:
                user.set_last_name(new_last_name)
                print("Atuallização realizada!")

    def update_house_number(self, user_name, new_house_number):
        for user in self.__list_users:
            if user.user_name == user_name:
                user.set_house_number(new_house_number)
                print("Atuallização realizada!")

    def update_street(self, user_name, new_street):
        for user in self.__list_users:
            if user.user_name == user_name:
                user.set_street(new_street)
                print("Atuallização realizada!")

    def update_postal_code(self, user_name, new_postal_code):
        for user in self.__list_users:
            if user.user_name == user_name:
                user.set_postal_code(new_postal_code)
                print("Atuallização realizada!")

    def update_email(self, user_name, new_email):
        for user in self.__list_users:
            if user.user_name == user_name:
                user.set_email(new_email)
                print("Atuallização realizada!")

    def update_birth_date(self, user_name, birth_date):
        for user in self.__list_users:
            if user.user_name == user_name:
                user.set_birth_date(birth_date)
                print("Atuallização realizada!")

    def add_user(self, user):
        self.__list_users.append(user)

    def find_user_by_user_name_and_print(self, user_name):
        for user in self.__list_users:
            if user.user_name == user_name:
                print("+--------------------------------+")
                print("Nome de usuário: ", user.user_name)
                print("Nome: ", user.name)
                print("Sobrenome: ", user.last_name)
                print("Número da casa: ", user.house_number)
                print("Rua: ", user.street)
                print("CEP: ", user.postal_code)
                print("Email: ", user.email)
                print("Data de nascimento: ", user.birth_date)
                print("+--------------------------------+")

    def find_user_by_user_name(self, user_name):
        for user in self.__list_users:
            if user.user_name == user_name:
                print("+--------------------------------+")
                print("Nome de usuário: ", user.user_name)
                print("Nome: ", user.name)
                print("Sobrenome: ", user.last_name)
                print("+--------------------------------+")
                user_found = {
                    "user_name": user.user_name,
                    "name": user.name,
                    "last_name": user.last_name,
                    "house_number": user.house_number,
                    "street": user.street,
                    "postal_code": user.postal_code,
                    "email": user.email,
                    "birth_date": user.birth_date,
                }
                return user_found

    def get_total(self):
        print("A quantidade de usuários é ", len(self.__list_users))
