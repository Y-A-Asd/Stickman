import csv

class Bank:
    users = []
    b_reserve = 9000
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance - self.b_reserve
        assert balance < 0 , "you dont have enough money"
        self.user = {}
        self.user["name"] = self.name
        self.user["balance"] = self.balance
        Bank.users.append(self.user)

    def withdraw(self,num):
        self.balance =  self.balance - num
        assert self.balance < 0, "you dont have enough money"
    def deposit(self,num):
        self.balance = self.balance + num
    @classmethod
    def csv_file(cls):
        with open ("bank_acc.csv","a")as accs:
            writer = csv.DictWriter(accs, fieldnames=["name", "balance"])
            writer.writerows(cls.users)
    # # creating a csv dict writer object
    # writer = csv.DictWriter(csvfile, fieldnames=fields)
    #
    # # writing headers (field names)
    # writer.writeheader()
    #
    # # writing data rows
    # writer.writerows(mydict)

acc1 = Bank("ahmad",30000)
acc2 = Bank("ali",50000)
print(Bank.users)
Bank.csv_file()
