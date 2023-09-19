import sqlite3
import hashlib

class NotEnoughMoney(Exception):
    pass
class BankAccount:
    min_balance = 1000
    def __init__(self, name, balance):
        if balance < BankAccount.min_balance:
            raise NotEnoughMoney
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute(f"UPDATE accounts SET BALANCE=BALANCE+{amount} WHERE NAME='{self.name}'")
        conn.commit()
        return "Done"

    def withdraw(self, amount):
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute(f"SELECT BALANCE FROM accounts WHERE NAME='{self.name}'")
        balance = c.fetchone()[0]
        if int(balance) - amount >= BankAccount.min_balance:
            c.execute(f"UPDATE accounts SET BALANCE=BALANCE-{amount} WHERE NAME='{self.name}'")
            conn.commit()
            return "Done"
        else:
            raise NotEnoughMoney (f"Sorry,u cant withdraw {self.name}!")

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)

    def str(self):
        return f"Account Holder: {self.name}\nAccount Balance: {self.balance}"




conn = sqlite3.connect('bank.db')

conn.execute('''CREATE TABLE IF NOT EXISTS accounts
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             NAME TEXT NOT NULL,
             BALANCE REAL NOT NULL);''')


account1 = BankAccount("ali ahmadi", 1000)
account2 = BankAccount("yousof asadi",800000 )
# conn.execute(f"INSERT INTO accounts (NAME, BALANCE) VALUES ('{account1.name}', {account1.balance})")
# conn.execute(f"INSERT INTO accounts (NAME, BALANCE) VALUES ('{account2.name}', {account2.balance})")
# conn.commit()
account1.deposit(10000)
account2.withdraw(90000)
account1.transfer(account2,15000)
conn.commit()
conn.close()


# def main():
#     try:
#         while True:
#             print("\nMenu:")
#             print("1. View Account Balance")
#             print("2. Deposit Money")
#             print("3. Withdraw Money")
#             print("4. Transfer Money")
#             print("5. Exit")
#
#             choice = input("Enter your choice (1/2/3/4/5): ")
#
#             if choice == '1':
#                 print(alice_account)
#             elif choice == '2':
#                 amount = float(input("Enter the amount to deposit: "))
#                 alice_account.deposit(amount)
#             elif choice == '3':
#                 amount = float(input("Enter the amount to withdraw: "))
#                 alice_account.withdraw(amount)
#             elif choice == '4':
#                 recipient_name = input("Enter the recipient's name: ")
#                 recipient_account = BankAccount(recipient_name, 0)  # Create a temporary recipient account
#                 amount = float(input("Enter the amount to transfer: "))
#                 alice_account.transfer(recipient_account, amount)
#             elif choice == '5':
#                 print("Exiting the program.")
#                 break
#             else:
#                 print("Invalid choice. Please choose a valid option (1/2/3/4/5).")
#
#     except NotEnoughMoney as e:
#         print(e)
# main()

























def men_u():
    try:
        database = r"cart.sqlite"
        conn = create_connection(database)
        options = ["login(conn,name=input('Username: '),password=input('Password: '))",
                   "signup(conn,name=input('Username: '),pass_stat=input('Do you want to generate an auto-generated password? (y/n): '))",
                   "show_products(conn,name=input('To display the entire list, simply press enter without entering any keywords.'))",
                   "insert_into_cart(conn,uproduct_name=input('Please provide the name of the product you want to add: '),product_count=int(input('Number: ')))",
                   "remove_from_cart(conn,name=input('Please indicate the name of the product\'n you liked to remove: '))",
                   "modify_cart(conn,product_name=input('Please specify the name of the product you want to change:'),new_number=int(input('New Value: ')))",
                   "show_cart(conn)",
                   "submit(conn)",
                   "exit('WELCOME {{Ysf.A.Asd}}')"
                   ]
        num_options=[1,2,3,4,5,6,7,8,9]
        while True:
            try:
                print("\n1. ADD PLAYER")
                print("2. SET PLAYER TO A TEAM")
                print("3. SHOW LIST OF PLAYER")
                print("4. ADD ITEM TO CART")
                print("5. REMOVE ITEM FROM CART")
                print("6. MODIFY YOUR CART")
                print("7. SEE MY CART")
                print("8. FINISH ORDERING")
                print("9. CANCEL EVERY THINGS AND LOG OUT\n")
                option = zip(num_options,options)
                user_choose = int(input("SELECT YOUR CHOICE (1-9): "))
                if 1 <= user_choose <= 9:pass
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
                for munes, funcs in option:
                    if user_choose == munes:
                        eval(funcs)
            except ValueError:
                print("Please try again, your input is invalid.")
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")