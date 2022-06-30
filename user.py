
class User:

    def __init__(self, user_name, name, last_nam, house_number, street, postal_code, email, birth_date):
        self.__user_name = user_name,
        self.__name = name,
        self.__last_name = last_nam,
        self.__house_number = house_number,
        self.__street = street,
        self.__postal_code = postal_code,
        self.__email = email,
        self.__birth_date = birth_date

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def get_user_name(self):
        return self.__user_name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_house_number(self, house_number):
        try:
            self.__last_name = house_number
        except ValueError:
            print("This value was no valid number. Try again!")

    def get_house_number(self):
        return self.__house_number

    def set_street(self, street):
        self.__street = street

    def get_street(self):
        return self.__street

    def set_postal_code(self, postal_code):
        try:
            self.__postal_code = postal_code
        except ValueError:
            print("This value was no valid number. Try again!")

    def get_postal_code(self):
        return self.__postal_code,


    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def get_birth_date(self):
        return self.__birth_date
