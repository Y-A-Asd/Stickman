# import sqlite3
#
#
# def create_table(conn, create_table_sql):
#     c = conn.cursor()
#     c.execute(create_table_sql)
#
#
# def main():
#     database = r"cart.sqlite"
#     sql_create = """ CREATE TABLE IF NOT EXISTS products (
#     id TEXT,
#     name TEXT,
#     gheymat TEXT
# );"""
#     sql_create1 = """ CREATE TABLE IF NOT EXISTS users (
#         id TEXT,
#         name TEXT,
#         password TEXT
#         );"""
#     sql_create2 = """ CREATE TABLE IF NOT EXISTS cart (
#         id TEXT,
#         user_name TEXT,
#         product_name TEXT,
#         product_gheymat TEXT,
#         product_count TEXT
#         );"""
#
#     conn = create_connection(database)
#     create_table(conn, sql_create)
#     create_table(conn, sql_create1)
#     create_table(conn, sql_create2)
#
#
# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     conn = sqlite3.connect(db_file)
#     return conn
#
#
# main()

#ITS WORKS..

# import sqlite3
#
#
# def create_table(conn, create_table_sql):
#     c = conn.cursor()
#     c.execute(create_table_sql)
#     print("Table created successfully")
#     conn.commit()
#
#
# def main():
#     database = r"cart.sqlite"
#     sql_create = """ CREATE TABLE IF NOT EXISTS products (
#         id TEXT,
#         name TEXT,
#         gheymat TEXT
#     );"""
#     sql_create1 = """ CREATE TABLE IF NOT EXISTS users (
#         id TEXT,
#         name TEXT,
#         password TEXT
#     );"""
#     sql_create2 = """ CREATE TABLE IF NOT EXISTS cart (
#         id TEXT,
#         user_name TEXT,
#         product_name TEXT,
#         product_gheymat TEXT,
#         product_count TEXT
#     );"""
#
#     conn = create_connection(database)
#     create_table(conn, sql_create)
#     create_table(conn, sql_create1)
#     create_table(conn, sql_create2)
#
#
# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     conn = sqlite3.connect(db_file)
#     print("Connection established successfully")
#     return conn
#
#
# main()
#LAST SQL GENERATOR:
# create table orders
# (
#     id          integer not null
#         constraint orders_pk
#             primary key autoincrement,
#     user_name   TEXT,
#     user_orders TEXT
# );
#
# create table products
# (
#     id      INTEGER not null
#         constraint products_pk
#             primary key autoincrement,
#     name    TEXT,
#     gheymat TEXT,
#     mojodi  integer
# );
#
# create table sqlite_master
# (
#     type     TEXT,
#     name     TEXT,
#     tbl_name TEXT,
#     rootpage INT,
#     sql      TEXT
# );
#
# create table sqlite_sequence
# (
#     name,
#     seq
# );
#
# create table users
# (
#     id       INTEGER not null
#         constraint users_pk
#             primary key autoincrement,
#     name     TEXT
#         constraint users_pk2
#             unique,
#     password TEXT,
#     loged    INTEGER default 0,
#     salers   integer default 0
# );
#
# create table cart
# (
#     id              INTEGER not null
#         constraint cart_pk
#             primary key autoincrement,
#     user_name       TEXT
#         constraint cart_users__fk
#             references users (name),
#     product_name    TEXT
#         constraint cart_products_name_fk
#             references products (name),
#     product_gheymat TEXT
#         constraint cart_products_gheymat_fk
#             references products (gheymat),
#     product_count   TEXT
# );


import sqlite3
import logging
import random
import string
from cryptography.fernet import Fernet
import key_enc
# key = bytes(b'TTmQ2md_rmJ0MRqgXFUvnLWkijkKTtcWVKJyz46mdD4=')
key = key_enc.key()
fernet = Fernet(key)
# encMessage = fernet.encrypt(message.encode())
# decMessage = fernet.decrypt(encMessage).decode()

def mydecorator(func):
    def process(*args, **kwargs):
        logging.basicConfig(filename='cart.log', level=logging.DEBUG, filemode='a', format='%(asctime)s-%(process)d-%(levelname)s-%(message)s')
        logging.debug(f"called function {func.__name__}")
        try:
            result = func(*args, **kwargs)
        except sqlite3.ProgrammingError:
            print("Something went wrong. Please try again!")
        logging.debug(f"{func.__name__} process done!")
        return result
    return process

@mydecorator
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = None
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error:
        print("Something went wrong. Please try again!")

@mydecorator
def reset_table(conn):
    """every time program start reset the tables to default"""
    try:
        c = conn.cursor()
      # c.execute("DELETE FROM cart")               #reset cart data
        c.execute("UPDATE users SET loged=0")       #reset user login status
        conn.commit()
        return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")

@mydecorator
def check_products(conn,name):
    """Check if product exist"""
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM products WHERE name=?", (name,))
        products = c.fetchone()
        if products is not None:
            # print(f"products {name} already exists!")
            return True
        else:
            # print("products does not exist.")
            return False
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
@mydecorator
def show_products(conn,name = None):
    """Print the list of products, optionally filtered by name."""
    try:
        c = conn.cursor()
        if name is not None:
            c.execute(f"SELECT * FROM products WHERE name LIKE '%{name}%' ")
        else:
            c.execute("SELECT * FROM products")
        products = c.fetchall()
        # for i in products:
        #     print(i)
        print("\n".join(str(product) for product in products))
        return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
@mydecorator
def add_products(conn,name,gheymat,mojodi):
    """Add item to products list"""
    try:
        c = conn.cursor()
        if check_products(conn,name):print(f"products {name} already exists!")
        else:
            c.execute("INSERT INTO products (name, gheymat,mojodi) VALUES (?, ?,?)", (name, gheymat,mojodi))
            conn.commit()
            print(f"product{name} added successfully!")
        return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
@mydecorator
def rm_products(conn,name):
    """Remove item from products list"""
    try:
        c = conn.cursor()
        if check_products(conn,name):
            status = input(f"ARE YOU SURE ABOUT REMOVING {name}?(y/n)")
            if status.lower() == "y":
                c.execute("DELETE FROM products WHERE name=?", (name,))
                print("products successful REMOVED.")
            else:return
        else:print("products does not exist.")
        return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")

@mydecorator
def generate_strong_password():
    length = 12
    num_uppercase = 2
    num_lowercase = 6
    num_digits = 2
    num_special_chars = 2
    uppercase_chars = ''.join(random.sample(string.ascii_uppercase, num_uppercase))
    lowercase_chars = ''.join(random.sample(string.ascii_lowercase, num_lowercase))
    digit_chars = ''.join(random.sample(string.digits, num_digits))
    special_chars = ''.join(random.sample(string.punctuation, num_special_chars))
    password = uppercase_chars + lowercase_chars + digit_chars + special_chars
    return ''.join(random.sample(password, length))
@mydecorator
def check_user(conn, name):
    """check if user exist"""
    global fernet
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE name=?", (name,))
        user = c.fetchone()
        if user is not None:
            # print(f"User {name} already exists!")
            return True
        else:
            # print("User does not exist.")
            return False
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
@mydecorator
def login(conn, name, password):
    """login process"""
    global fernet
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE loged=1")
        status = c.fetchall()
        assert status == []                               #if user already logged
        if not check_user(conn, name):             #if user not exist
            print("User does not exist.")
            exit()
        else:
            c.execute("SELECT password FROM users WHERE name=?", (name,))
            user_pass = c.fetchone()
            if user_pass is not None:
                dec_password = fernet.decrypt(user_pass[0]).decode()
                if str(dec_password) == str(password):
                    print(f"Login successful as {name}!")
                    c.execute("UPDATE users SET loged=1 WHERE name=?", (name,))
                    conn.commit()
                else:
                    print("Invalid password")

            else:
                print("Invalid username")
        return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
    except AssertionError:
        print(f"you already logged in as {status[0][0]} ")
@mydecorator
def signup(conn, name, pass_stat):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE loged=1")
        status = c.fetchall()
        assert status == []
        if check_user(conn, name) :
            print(f"User {name} already exists!")
        else:
            if pass_stat.lower() == "y":
                password = generate_strong_password()
            else:
                password = input("Password: ")
            enc_password = encMessage = fernet.encrypt(password.encode())
            c.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, enc_password))
            conn.commit()
            print(f"User {name} created successfully!")
            print(f"You logged in as : {name}")
            c.execute("UPDATE users SET loged=1 WHERE name=?", (name,))
            conn.commit()
        return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
    except AssertionError:
        print(f"you already logged in as {status[0][0]} ")

@mydecorator
def check_into_cart(conn, name):
    try:
        c = conn.cursor()
        # Retrieve the names of all logged-in users
        c.execute("SELECT name FROM users WHERE loged=1")
        logged_in_users = c.fetchall()
        for user in logged_in_users:
            user_name = user[0]
            # Check if the product exists in the cart for the current user
            c.execute("SELECT * FROM cart WHERE user_name=? AND product_name=?", (user_name, name))
            cart_entry = c.fetchone()
            if cart_entry is not None:
                return True
        return False
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
@mydecorator
def insert_into_cart(conn,uproduct_name, product_count):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE loged=1")
        user_name = c.fetchone()[0]
    except Exception:
        print("Please login first!")
        return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
        return
    if check_into_cart(conn,uproduct_name):
        print(f"products {uproduct_name} already exists in your cart")
    else:
        if check_products(conn,uproduct_name):
            c = conn.cursor()
            c.execute(f"SELECT name FROM products WHERE name LIKE '%{uproduct_name}%' ")
            product_name = c.fetchone()[0]
            c.execute(f"SELECT gheymat FROM products WHERE name LIKE '%{uproduct_name}%' ")
            product_gheymat = c.fetchone()[0]
            c.execute(f"SELECT mojodi FROM products WHERE name LIKE '%{uproduct_name}%' ")
            mojodi = c.fetchone()[0]
            if int(mojodi) > 0:
                c.execute("INSERT INTO cart (user_name, product_name, product_gheymat, product_count) VALUES (?, ?, ?, ?)",
                      (user_name, product_name, product_gheymat, product_count))
                print("product added!")
            else:print(f"We don't have the requested quantity of {product_name} in stock.")
            conn.commit()
        else:print(f"Product ({uproduct_name}) does not exist!")
@mydecorator
def remove_from_cart(conn,name):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE loged=1")
        user = c.fetchall()
        assert user != []
        if check_into_cart(conn, name):
            status = input(f"ARE YOU SURE ABOUT REMOVING {name}?(y/n)")
            if status.lower() == "y":
                c.execute("DELETE FROM cart WHERE product_name=? AND user_name=?", (name,user[0][0]))
                print(f"product {name} successful REMOVED from your cart.")
                conn.commit()
                return
            else:
                return
        else:
            print(f"products {name} does not exist in your cart.")
            return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
    except AssertionError:
        print("Please login first!")
@mydecorator
def modify_cart(conn,product_name,new_number):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE loged=1")
        user = c.fetchall()
        assert user != []
        try:
            c.execute("UPDATE cart SET product_count=? WHERE user_name=? AND product_name=?", (new_number,user[0][0],product_name))
        except Exception:
            print(f"There is no {product_name} in your cart to modify.")
        conn.commit()
        print("Changes have been successfully made.")
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
    except AssertionError:
        print("Please login first!")
    return
@mydecorator
def show_cart(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE loged=1")
        status = c.fetchall()
        assert status != []
        c.execute("SELECT * FROM cart WHERE user_name=?",(status[0][0],))
        print_cart = c.fetchall()
        print("\n".join(str(product) for product in print_cart))
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
    except AssertionError:
        print("Please login first!")

@mydecorator
def submit(conn):
    try:
        payment = 0
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE loged=1")
        status = c.fetchall()
        assert status != [],("Please login first!")
        user_name = status[0][0]
        c.execute("SELECT * FROM cart WHERE user_name=?", (user_name,))
        carts = c.fetchall()
        c.execute("SELECT product_name FROM cart WHERE user_name=?", (user_name,))
        products = c.fetchall()
        c.execute("SELECT product_gheymat From cart WHERE user_name=?", (user_name,))
        pay = c.fetchall()
        c.execute("SELECT product_count From cart WHERE user_name=?", (user_name,))
        number = c.fetchall()
        num_incart = len(number)
        for i in range(num_incart):
            assert check_cart(conn,user_name,products[i][0]),(f"Your cart contains {products[i][0]} with modified quantities, preventing submission.")
        for i in range(num_incart):
            payment += int(pay[i][0]) * int(number[i][0])
        print("Your cart:")
        print("\n".join(str(product) for product in carts))
        print("TOTAL:")
        print(payment)
        cart_pay(conn,user_name,products,number)
        for i in range(num_incart):
            update_products_list(conn,products[i][0],number[i][0])
        #RESET CART
        c.execute("DELETE FROM cart WHERE user_name=?", (user_name,))
        conn.commit()
        exit('WELCOME {{Ysf.A.Asd}}')

    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
    except AssertionError as error:
        print(error)

@mydecorator
def cart_pay(conn,user_name,product_name,product_count):
    try:
        number = len(product_count)
        orderd ={}
        for i in range(number):
            orderd.update(dict(zip(product_name[i] , product_count[i])))
        c = conn.cursor()
        if orderd == {}:
            print("Your shopping cart is currently empty.")
        else:
            c.execute("INSERT INTO orders (user_name, user_orders) VALUES (?, ?)",(user_name,str(orderd)))
            conn.commit()
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")

@mydecorator
def check_cart(conn,user_name,product_name):
    try:
        c = conn.cursor()
        c.execute(f"SELECT mojodi FROM products WHERE name LIKE '%{product_name}%' ")
        mojodi = c.fetchone()[0]
        c.execute("SELECT product_count From cart WHERE user_name=?", (user_name,))
        number = c.fetchone()[0]
        if int(mojodi) >= int(number):
            return True
        else:
            return False
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")

@mydecorator
def update_products_list(conn,product_name,product_used):
    try:
        c = conn.cursor()
        c.execute(f"SELECT mojodi FROM products WHERE name LIKE '%{product_name}%' ")
        mojodi = c.fetchone()[0]
        updated_user = int(mojodi) - int(product_used)
        c.execute("UPDATE products SET mojodi = ? WHERE name=?", (updated_user,product_name))
        conn.commit()
        return
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")

@mydecorator
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
                print("\n1. LOGIN")
                print("2. SINGING")
                print("3. SHOW LIST OF PRODUCTS")
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

@mydecorator
def main():
    try:
        database = r"cart.sqlite"
        conn = create_connection(database)
        reset_table(conn)
        men_u()
    except sqlite3.ProgrammingError:
        print("Something went wrong. Please try again!")
    except KeyboardInterrupt:
        print("\nGOODBYE")
        exit('WELCOME {{Ysf.A.Asd}}')
main()

#YOUSOF.A.ASADI
#THANCKS REACH DOWN HEAR

#FUTURE UPDATES:
#TODO:ENCRYPTING PASSWORD , DONE
#TODO:AUTO GENERATE PASSWORD , DONE

#TODO:SALERS PANEL , UPCOMING SONE...
#TODO:WORK WITH CALSSES , UPCOMING SONE...


