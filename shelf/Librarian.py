import itertools
from Shelf import Shelf
class Librarian(object):
    def __init__(self, name: str):
        self.name = name


    @staticmethod
    def search( book_name=None, book_id=None, book_author=None):
        result_list = []
        original_list = list(itertools.chain.from_iterable(Shelf.book_shelf.items()))
        for shelfs, sub_list in zip(original_list[::2], original_list[1::2]):
            if isinstance(sub_list, list):
                for book_in_shelf in sub_list:
                    if (book_name is None or book_in_shelf.name == book_name) and \
                        (book_id is None or book_in_shelf.__unique_id == book_id) and \
                        (book_author is None or book_in_shelf.__author == book_author):
                        result_list.append({shelfs: book_in_shelf})
        return result_list

        # [1234321, [<__main__.Books object at 0x7f5ab4060710>, <__main__.Books object at 0x7f5ab39f3150>],
        # 3456,[<__main__.Books object at 0x7f5ab39f3150>]]





    @staticmethod
    def retrieve(unique_id: int):
        if slist := Librarian.search(book_id=unique_id):
            return slist
        else:
            print("book not found")
        pass

    def change_book_location(unique_id: int, new_location):
        current_location = search
        pass


    def add_book(self, book: object, location: str):
        pass

    @staticmethod
    def add_category(category_name : str):
        # Category.add_category(category_name)
        # return none
        pass
"""
Librarian->name
- search-> book_name=None, book_id=None, book_author=None
- retrieve->unique_id
- change_book_location->
"""