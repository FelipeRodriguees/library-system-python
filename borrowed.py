
class Borrowed:

    def __init__(self):
        self.borrowed = []

    @property
    def borrowed(self):
        return self.borrowed

    def set_borrowed(self, book):
        self.borrowed.append(book)