from homework_5.Book import Book

class Books:
    __books = []

    def __init__(self):
        book = Book("Harry Potter and the Philosopher's Stone", 1997, 15)
        book.set_authors("J. K. Rowling")
        self.__books.append(book)

        book = Book("Harry Potter and the Chamber of Secrets", 1998, 20)
        book.set_authors("J. K. Rowling")
        self.__books.append(book)

        book = Book("Harry Potter and the Prisoner of Azkaban", 1999, 22)
        book.set_authors("J. K. Rowling")
        self.__books.append(book)

        book = Book("The Road", 2006, 18)
        book.set_authors("Cormac McCarthy")
        self.__books.append(book)

        book = Book("Good Omens", 1990, 14)
        book.set_authors("Neil Gaiman", "Terry Pratchett")
        self.__books.append(book)

        book = Book.create_folk("Three Bears", 9)
        self.__books.append(book)

    @staticmethod
    def add_book(book):
        Books.__books.append(book)

    @staticmethod
    def delete_book(book):
        Books.__books.remove(book)

    @staticmethod
    def print_books():
        for book in Books.__books:
            print(book)

    @staticmethod
    def find_by_author(author):
        books = []
        for book in Books.__books:
            if book.__eq__(author):
                books.append(book)
        return books

    @staticmethod
    def find_over_year(year):
        books = []
        for book in Books.__books:
            if book.get_year() is None:
                continue
            elif book.__ge__(year):
                books.append(book)
        return books
