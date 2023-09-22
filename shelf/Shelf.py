import uuid


class Books:
    """
    کلاس کتاب
    """


    def __init__(self, book_id, name, author, pages):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.pages = pages


    def __len__(self):
        return self.pages

    def __repr__(self):
        return f"ID: {self.book_id}, NAME: {self.name}, AUTHOR: {self.author}, PAGEs: {self.pages}"

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

    # def __add__(self, book: Books):  # میتوان با اضافه کردن کتاب به قفسه آن را وارد قفسه کرد
    #     Shelf.book_shelf[self.shelf_id].append(book)
    #     return self

    def __len__(self):
        return len(Shelf.book_shelf[self.shelf_id])


class Author:
    def __init__(self,name,book):
        self.name = name
        if book not in self.books:
            self.books = [book]





book1 = Books(138434, "death", "mac kart", 397)
book2 = Books(352, "lives", "jaimse", 223)
book3 = Books(56700987, "end", "emad", 1008)
shelf1 = Shelf(10000)
shelf1.add_shelf(book1, book2, book3)
print(Shelf.book_shelf)




