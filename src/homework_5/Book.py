class Book:
    __id_count = 0
    __id = 0
    __title = ''
    __authors = []
    __publisher = ''
    __year = 0
    __pages = 0
    __price = 0
    __cover = ''

    def __init__(self, title, year):
        self.__title = title
        self.__year = year
        Book.__id_count += 1
        self.__id = Book.__id_count

    def __str__(self):
        return  "id: " + str(self.__id) + "\ntitle: " + self.__title + "\nauthors: " + str(self.__authors) + "\nyear: " + str(self.__year)

    @classmethod
    def create_folk(cls, title):
        book = cls(title, None)
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

