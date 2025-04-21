class Book:
    __id_count = 0

    def __new__(cls, *args, **kwargs):
        Book.__id_count += 1
        return object.__new__(cls)

    def __init__(self, title, year, price):
        self.__title = title
        self.__year = year
        self.__price = price
        self.__id = Book.__id_count

    def __del__(self):
        Book.__id_count -= 1

    def __str__(self):
        return  "id: " + str(self.__id) + "\ntitle: " + self.__title + "\nauthors: " + str(self.__authors) + '\nyear: '\
            + str(self.__year) + "\nprice: " + str(self.__price)

    def __setattr__(self, key, value):
        if key == 'discount':
            self.__price = self.__price * (1 - value / 100)
        else:
            self.__dict__[key] = value

    def __iadd__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Right operand should be int")
        self.__price += other
        return self

    def __imul__(self, other):
        if not isinstance(other, (float, int)):
            raise ArithmeticError("Right operand should be float or int")
        self.__price *= other
        return self

    def __eq__(self, other):
        if not isinstance(other, str):
            return False
        if other in self.__authors:
            return True
        else: return False

    def __ge__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Right operand should be int")
        return True if self.__year >= other else False

    @classmethod
    def create_folk(cls, title, price):
        book = cls(title, None, price)
        book.set_authors("Folk Work")
        return book

    @staticmethod
    def __is_positive(number):
        if number > 0 or number is None:
            return True
        elif number <= 0:
            print("Incorrect input, should be positive")
            return False

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_authors(self):
        return self.__authors

    def set_authors(self, *authors):
        self.__authors = authors[0] if len(authors) == 1 else authors

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if Book.__is_positive(year):
            self.__year = year

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        if Book.__is_positive(pages):
            self.__pages = pages

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if Book.__is_positive(price):
            self.__price = price

    def get_cover(self):
        return self.__cover

    def set_cover(self, cover):
        self.__cover = cover

