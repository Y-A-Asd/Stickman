import uuid
from pickle import PickleHandler
from book import Book
from Librarian import Librarian

class Shelf:
    """
    کلاس قفسه
    """
    book_shelf = {}

    def __init__(self, capacity):
        self.shelf_id = str(uuid.uuid4())
        self.capacity = capacity
        Shelf.book_shelf[self.shelf_id] = []
    def add_shelf(self, *books):
        Shelf.book_shelf[self.shelf_id].extend(books)

    def __add__(self, book: Books):  # میتوان با اضافه کردن کتاب به قفسه آن را وارد قفسه کرد
        Shelf.book_shelf[self.shelf_id].append(book)
        return self

    def __len__(self):
        return len(Shelf.book_shelf[self.shelf_id])


#Book : name, page_count, price, category, author
book1 = Book("death",200 ,1000,"Action","Ali")
book1 = Book("death",200 ,1000,"Action","Ali")
book1 = Book("death",200 ,1000,"Action","Ali")

shelf1 = Shelf(10000)
shelf1.add_shelf(book1, book2, book3)
print(Shelf.book_shelf)
pic = PickleHandler("book.pickle")
pic.write(Shelf.book_shelf)









