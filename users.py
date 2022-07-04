class Users:
    def __init__(self):
        self.__list_users = []

    def serializer(self, user):
        __user = {
            "user_name": user.user_name,
            "name": user.name.title(),
            "last_name": user.last_name.title(),
            "house_number": user.house_number,
            "street": user.street.title(),
            "postal_code": user.postal_code,
            "email": user.email,
            "birth_date": user.birth_date,
        }
        return __user

    def add_user(self, user):
        self.__list_users.append(self.serializer(user))

    def find_user_by_user_name_and_print(self, user_name):
        for user in self.__list_users:
            if user["user_name"] == user_name:
                print("+--------------------------------+")
                print("Nome de usuário: ", user["user_name"])
                print("Nome: ", user["name"])
                print("Sobrenome: ", user["last_name"])
                print("Número da casa: ", user["house_number"])
                print("Rua: ", user["street"])
                print("CEP: ", user["postal_code"])
                print("Email: ", user["email"])
                print("Data de nascimento: ", user["birth_date"])
                print("+--------------------------------+")

    def find_user_by_user_name(self, user_name):
        for user in self.__list_users:
            if user["user_name"] == user_name:
                print("+--------------------------------+")
                print("Nome de usuário: ", user["user_name"])
                print("Nome: ", user["name"])
                print("Sobrenome: ", user["last_name"])
                print("+--------------------------------+")
                user_found = {
                    "user_name": user["user_name"],
                    "name": user["name"],
                    "last_name": user["last_name"],
                    "house_number": user["house_number"],
                    "street": user["street"],
                    "postal_code": user["postal_code"],
                    "email": user["email"],
                    "birth_date": user["birth_date"],
                }
                return user_found

    def get_total(self):
        print("A quantidade de usuários é ", len(self.__list_users))
