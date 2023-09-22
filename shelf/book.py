class Book:

    counter = 0

    def init(self,name, page_count, price, category, author):

        self.name = name

        self.__unique_id = Book.counter

        self.__page_count = page_count

        self.__price = price

        self.__category = category

        self.__author = author

        Book.counter += 1


    def getter (self):
        return {"name" : self.name, "unique_id" : self.__unique_id, "page_count" : self.__page_count, "price" : self.__price, "category" : self.__category, "author" : self.__author}

    def show (str):
        return f"name : {self.name}, unique_id : {self.__unique_id}, page_count : {self.__page_count}, price : {self.__price}, category : {self.__category}, author : {self.__author}"


#
# a = Book()
#
# print(a.getter()["page_count"])