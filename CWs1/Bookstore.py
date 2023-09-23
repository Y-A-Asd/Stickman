import itertools
from datetime import date
import pickle



class PickleHandler:

    FILENAME = "FILE.pickle"
    @classmethod
    def write(cls,data):
        with open(cls.FILENAME, 'wb') as f:
            pickle.dump(data, f)
    @classmethod
    def read(cls,name):
        if cls.FILENAME:
            with open(cls.FILENAME, 'rb') as f:
                if f:
                    data = pickle.load(f)
                    print(data)
                    print()
                    print()
                    print()
                    print()
                    return data[0]
                    # print(data)
                    # for obj in list(data):
                    #     print(obj)
                    # if data.name == name:
                    #     print(data.name)
                    #     print("found")
                    # return data

class Books:
    """
    کلاس کتاب
    """
    all_books_count = 0

    def __init__(self, book_id, name, author, pages, cost, group=None):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.pages = pages
        self.cost = cost
        self.group = group
        Books.all_books_count += 1

    def __len__(self):
        return self.pages

    # def __repr__(self):
    #     return f"ID: {self.book_id}, NAME: {self.name}, AUTHOR: {self.author}, PAGEs: {self.pages}, COST: {self.cost}, TAKEN: {self.taken}"

class Grouping:
    """
    کلاس دسته بندی ها
    """
    grouping = {}
    def __init__(self,new_grouping):
        self.name = new_grouping
        Grouping.grouping[self.name] = []
    def __add__(self, book: Books):#میتوان به اضافه کردن کتاب به دسته بندی آن را وارد درسته بندی کرد
        Grouping.grouping[self.name].append(book)
        return self

class BookShelf:
    """
    :atter:
    :argumets:
    """
    book_shelf = {}
    shelev = []

    def __init__(self, shelf_id):
        self.shelf_id = shelf_id
        BookShelf.book_shelf[self.shelf_id] = []
        BookShelf.shelev.append(self)

    def __add__(self, book: Books):#میتوان با اضافه کردن کتاب به قفسه آن را وارد قفسه کرد
        BookShelf.book_shelf[self.shelf_id].append(book)
        return self

    def __len__(self):
        return len(BookShelf.book_shelf[self.shelf_id])

class People:
    """کلاس انسان"""
    def __init__(self, name,date):
        self.name = name
        self.date = date
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,newname):
        print ("seter called")
        if len(newname) < 2 or not all([char.isalpha() for char in newname]) :
            raise Exception("Invalid input")
        self.__name = newname
    @property
    def age(self):
        return date.today() - self.date

class Librarian(People,PickleHandler):
    """
    کلاس کتابدار
    """
    # FILENAME = "Librarian.pickle"
    list1 = []
    def __init__(self, name,date, person_id):
        super().__init__(name,date)
        print("LIb")
        a = PickleHandler.read(self.name)
        print(a.name)
        self.person_id = person_id
        Librarian.list1.append(self)
        PickleHandler.write(Librarian.list1)

    def search(self, book_name=None, book_id=None, book_author=None):
        """
        جستجو کتاب
        """
        result_list = []
        original_list = list(itertools.chain.from_iterable(BookShelf.book_shelf.items()))
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
        if len(book) == 1:
            # list(book[0].values())[0].taken = True
            return list(book[0].values())
        else:
            print("No books found!")
            return None

    def change_book_location(self,unique_id: int, new_location):
        current_location = list(self.search(book_id=unique_id)[0].items())
        BookShelf.book_shelf[current_location[0][0]].remove(current_location[0][1])
        # print(current_location[0])
        # print(current_location[0][1])
        # print(current_location[0][2])
        for i in BookShelf.shelev:
            if i.shelf_id == new_location:
                i+current_location[0][1]
    def add_book(self,shelf_id,book:Books):
        for i in BookShelf.shelev:
            if i.shelf_id == shelf_id:
                i+book
    def add_group(self,name,*args):
        group = Grouping(name)
        for book in args:
            group + book




shelf1 = BookShelf(1234321)
shelf2 = BookShelf(3415)
# print(BookShelf.book_shelf)
book1 = Books(138434, "death", "mac kart", 397, 1000)
book2 = Books(352, "lives", "jaimse", 223, 10000)
book3 = Books(56700987, "end", "emad", 1008, 100000)
shelf1 + book1 + book2 + book3
l1 = Librarian("ali",date.today(),12)
l2 = Librarian("mamad",date.today(),13)
# print(l1.age)
# # l1.name = "shayan"
# print(l1.name)
# # print(type(l1))
# print(len(shelf2))
# print(l1.search(book_id=352))
# l1.change_book_location(352,3415)
# print(l1.get_book(book_id=352))
# print(len(book1))
print(len(shelf1))
# l1.add_book(1234321,book2)
# print(len(shelf1))
# print(len(shelf2))
# l1.add_group("Action",book1,book2)
# print(Grouping.grouping)
# print(list(itertools.chain.from_iterable(BookShelf.book_shelf.values())))
