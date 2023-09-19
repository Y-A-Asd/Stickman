import itertools


class Books:
    """
    کلاس کتاب
    """
    all_books_count = 0

    def __init__(self, book_id, name, author, pages, cost, taken=False):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.pages = pages
        self.cost = cost
        self.taken = taken
        Books.all_books_count += 1

    def __len__(self):
        return self.pages

    def __repr__(self):
        return f"ID: {self.book_id}, NAME: {self.name}, AUTHOR: {self.author}, PAGEs: {self.pages}, COST: {self.cost}, TAKEN: {self.taken}"



class Grouping:
    """
    کلاس دسته بندی ها
    """
    grouping = {}
    def __init__(self,new_grouping):
        Grouping.grouping[new_grouping] = []
    def __add__(self, book: Books):#میتوان به اضافه کردن کتاب به دسته بندی آن را وارد درسته بندی کرد
        Grouping.grouping[self.grouping].append(book)
        return self



class BookShelf:
    """
    کلاس قفسه
    """
    book_shelf = {}

    def __init__(self, shelf_id):
        self.shelf_id = shelf_id
        BookShelf.book_shelf[self.shelf_id] = []

    def __add__(self, book: Books):#میتوان با اضافه کردن کتاب به قفسه آن را وارد قفسه کرد
        BookShelf.book_shelf[self.shelf_id].append(book)
        return self

    def __len__(self):
        return len(BookShelf.book_shelf[self.shelf_id])


class People:
    """کلاس انسان"""
    def __init__(self, name):
        self.name = name


class Librarian(People):
    """
    کلاس کتابدار
    """
    def __init__(self, name, person_id):
        super().__init__(name)
        self.person_id = person_id

    def search(self, book_name=None, book_id=None, book_author=None):
        """
        جستجو کتاب
        """
        result_list = []
        original_list = list(itertools.chain.from_iterable(Shelf.book_shelf.items()))
        # [1234321, [<__main__.Books object at 0x7f5ab4060710>, <__main__.Books object at 0x7f5ab39f3150>], 3415,
        # [<__main__.Books object at 0x7f5ab39f3150>]]

        for shelfs, sub_list in zip(original_list[::2], original_list[1::2]):
            if isinstance(sub_list, list):
                for book_in_shelf in sub_list:
                    """شرط به این صورت است که اگر مقادیر خالی باشند در نظر گرفته نمی شوند ولی اگر وجود داشته باشند طبق هر چند شرط فیلتر میشود"""
                    if (book_name is None or book_in_shelf.name == book_name) and \
                            (book_id is None or book_in_shelf.book_id == book_id) and \
                            (book_author is None or book_in_shelf.author == book_author):
                        result_list.append({shelfs: book_in_shelf})

        return result_list
        # for books     in list(itertools.chain.from_iterable(BookShelf.book_shelf.values())):
        #     if books.name == book_name or books.book_id == book_id or books.author == book_author :
        #         return books

    @staticmethod
    def add_shelf(shelf_id: int) -> BookShelf:
        """
        اضافه کردن قفسه
        """
        new_shelf = BookShelf(shelf_id)
        return new_shelf

    def get_book(self, book_name=None, book_id=None, book_author=None):
        """
        قرض گرفتن کتاب
        """
        book = Librarian.search(self, book_name=book_name, book_id=book_id, book_author=book_author)
        if len(book) > 1:#اگر کتاب در چندین قفسه وجود داشت
            print("multiply books found choose one!")
            print(list(itertools.chain.from_iterable(book)))
            chosse = int(input("Select Shelfs: "))
            for sames in book:
                for k, v in sames.items():
                    if k == chosse:
                        v.taken = True
                        return v
        elif len(book) == 1:
            list(book[0].values())[0].taken = True
            return list(book[0].values())
        else:
            print("No books found!")
            return None

    def pass_book(self, book_name=None, book_id=None, book_author=None):
        """
        پس دادن کتاب
        """
        book = Librarian.search(self, book_name=book_name, book_id=book_id, book_author=book_author)
        if len(book) > 1:#اگر کتاب در چندین قفسه وجود داشت
            print("multiply books found choose one!")
            print(list(itertools.chain.from_iterable(book)))
            chosse = int(input("Select Shelfs: "))
            for sames in book:
                for k, v in sames.items():
                    if k == chosse:
                        if v.taken:
                            v.taken = False
                            return v
                        else:
                            print("This book is not taken!")
                            return None
        elif len(book) == 1:
            if list(book[0].values())[0].taken:
                list(book[0].values())[0].taken = False
                return list(book[0].values())
            else:
                print("This book is not taken!")
                return None
        else:
            print("No books found!")
            return None


shelf1 = BookShelf(1234321)
shelf2 = BookShelf(3415)
# print(BookShelf.book_shelf)
book1 = Books(138434, "death", "mac kart", 397, 1000)
book2 = Books(352, "lives", "jaimse", 223, 10000)
book3 = Books(56700987, "end", "emad", 1008, 100000)
shelf1 + book1 + book2 + book3
shelf2 + book2
l1 = Librarian("ali", 14214)
# print(l1.search(book_id=352))
print(l1.get_book(book_id=138434))
print(len(book1))
print(len(shelf1))
# print(list(itertools.chain.from_iterable(BookShelf.book_shelf.values())))
