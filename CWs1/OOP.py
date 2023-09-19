# class Students:
#     pass
# class Marks:
#     pass
# students = Students()
# marks = Marks()
#
# stu_ins = isinstance(students, Students)
# mrk_ins = isinstance(marks, Marks)
#
# stu_sub = issubclass(Marks, object)
# mrk_sub = issubclass(Students, object)
#
# print(stu_ins)
# print(mrk_ins)
# print(stu_sub)
# print(mrk_sub)
#


# class rec:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area (self):
#         return self.length * self.width
# rec1 = rec(5,6)
# print(rec1.area())


# class Bank:
#     def __init__(self, balance, name, accountNumber):
#         self.balance = balance
#         self.name = name
#         self.accountNumber = accountNumber
#
#     def deposit(self, amount):
#             self.balance += amount
#             print(f"balance: {self.balance}")
#
#
#     def withdrawal(self, amount):
#         self.balance -= amount
#         print(f"withdrawal: {self.balance}")
#
#     def bankFees(self):
#         self.balance = self.balance * 0.95
#         print(f"balance: {self.balance}")
#     def display(self):
#         print(f"acc number: {self.accountNumber}")
#         print(f"name: {self.name}")
#         print(f"balance: {self.balance}")
#
# account1 = Bank(1000, "yousof", "12345")
#
# account1.deposit(500)
# account1.withdrawal(200)
# account1.bankFees()
#
# account1.display()


# class Smartphone:
#     def __init__(self, brand, model, system, size, storage):
#         self.brand = brand
#         self.model = model
#         self.system = system
#         self.screen_size = size
#         self.storage = storage
#         self.battery = 100
#         self.apps = []
#
#     def playgame(self, name):
#         if name in self.apps:
#             self.battery = 50
#             return "playing"
#
#     def install_app(self, app_name):
#         self.apps.append(app_name)
#         return f"inestalled {app_name}"
#
#     def charge(self):
#         self.battery = 99
#     def display_info(self):
#         b=f"brand: {self.brand}"
#         m=f"model: {self.model}"
#         s=f"system: {self.system}"
#         si=f"size: {self.screen_size} inches"
#         ba=f"battery : {self.battery}"
#         st=f"storage: {self.storage} GB"
#         ap=f"apps: {', '.join(self.apps)}"
#         return f"{b}\n{m}\n{s}\n{si}\n{ba}\n{st}\n{ap}"
#
#
# my_phone = Smartphone("iphone", "X", "IOS", 6.4, 128)
# print(my_phone.display_info())
# print(my_phone.install_app("gta_v"))
# print(my_phone.playgame("gta_v"))
# my_phone.charge()
# print(my_phone.display_info())

def hello(name):
    txt = "hello" + name
    print(txt)
hello("yousof")
