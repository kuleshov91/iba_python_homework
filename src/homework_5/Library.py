from homework_5.Books import Books

Books()
Books.print_books()
print("-----------------J. K. Rowling-----------------------")
books = Books.find_by_author("J. K. Rowling")
for book in books:
    book.discount = 10
    print(book)
print("-----------------over 1999-----------------------")
books = Books.find_over_year(1999)
for book in books:
    book.__iadd__(10)
    print(book)
print("-----------------multiple-----------------------")
for book in books:
    book.__imul__(1.2)
    print(book)
print("----------------------------------------")