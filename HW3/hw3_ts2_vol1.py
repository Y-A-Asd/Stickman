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


import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    conn = sqlite3.connect(db_file)
    return conn
def reset_table(conn):
    """every time program start reset the tables to default"""
    c = conn.cursor()
    c.execute("DELETE FROM cart")               #reset cart data
    c.execute("UPDATE users SET loged=0")       #reset user login status
    conn.commit()
    return



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
        print("something goes off pls try again!")
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
        print("something goes off pls try again!")
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
        print("something goes off pls try again!")
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
        print("something goes off pls try again!")



def check_user(conn, name):
    """check if user exist"""
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
        print("something goes off pls try again!")
def login(conn, name, password):
    """login process"""
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE loged=1")
        status = c.fetchall
        assert status == None                               #if user already logged
        if not check_user(conn, name):                      #if user not exist
            print("User does not exist.")
            exit()
        else:
            c.execute("SELECT * FROM users WHERE name=? AND password=?", (name, password))
            user = c.fetchone()
            if user is not None:
                print(f"Login successful as {name}!")
                c.execute("UPDATE users SET loged=1 WHERE name=?", (name,))
                conn.commit()
            else:
                print("Invalid username or password.")
        return
    except sqlite3.ProgrammingError:
        print("something goes off pls try again!")
    except AssertionError:
        print("you already logged in!")
def signup(conn, name, password):
    try:
        c = conn.cursor()
        if check_user(conn, name) :
            print(f"User {name} already exists!")
            exit()
        else:
            c.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
            conn.commit()
            print(f"User {name} created successfully!")
            print(f"You logged in as : {name}")
            c.execute("UPDATE users SET loged=1 WHERE name=?", (name,))
            conn.commit()
        return
    except sqlite3.ProgrammingError:
        print("something goes off pls try again!")
def auto_password():pass                #This feature will be activated in the future



def check_into_cart(conn,name):
    c = conn.cursor()
    c.execute("SELECT * FROM cart WHERE product_name=?", (name,))
    carts = c.fetchone()
    if carts is not None:
        # print(f"products {name} already exists!")
        return True
    else:
        # print("products does not exist.")
        return False
def insert_into_cart(conn,uproduct_name, product_count):
    if check_into_cart(conn,uproduct_name):
        print(f"products {uproduct_name} already exists in your cart")
    else:
        if check_products(conn,uproduct_name):
            c = conn.cursor()
            c.execute(f"SELECT name FROM products WHERE name LIKE '%{uproduct_name}%' ")
            product_name = c.fetchone()[0]
            c.execute(f"SELECT gheymat FROM products WHERE name LIKE '%{uproduct_name}%' ")
            product_gheymat = c.fetchone()[0]
            try:
                c.execute("SELECT name FROM users WHERE loged=1")
                user_name = c.fetchone()[0]
            except Exception:
                print("Please login first!")
                return
            c.execute(f"SELECT mojodi FROM products WHERE name LIKE '%{uproduct_name}%' ")
            mojodi = c.fetchone()[0]
            if int(mojodi) > 0:
                c.execute("INSERT INTO cart (user_name, product_name, product_gheymat, product_count) VALUES (?, ?, ?, ?)",
                      (user_name, product_name, product_gheymat, product_count))
            else:print(f"we dont have mojodi for {product_name}")
            conn.commit()
            conn.close()
        else:print(f"Product ({uproduct_name}) does not exist!")
def remove_from_cart(conn,name):
    c = conn.cursor()
    if check_into_cart(conn, name):
        status = input(f"ARE YOU SURE ABOUT REMOVING {name}?(y/n)")
        if status.lower() == "y":
            c.execute("DELETE FROM cart WHERE product_name=?", (name,))
            print(f"product {name} successful REMOVED from your cart.")
            conn.commit()
            return
        else:
            return
    else:
        print(f"products {name} does not exist in your cart.")
        return
def show_cart(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM cart")
    print_cart = c.fetchall()
    print("\n".join(str(product) for product in print_cart))



def submit(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM cart")
    print_cart = c.fetchall()
    c.execute("SELECT product_gheymat From cart")
    result_pay = c.fetchall()
    print("Your cart:")
    print("\n".join(str(product) for product in print_cart))
    print("TOTAL:")
    print(result_pay)
    print("WELCOME {Ysf.A.Asd}")
    exit()


def men_u():
    database = r"cart.sqlite"
    conn = create_connection(database)
    options = ["login(conn,name=input('Username: '),password=input('Password: '))",
               "signup(conn,name=input('Username: '),password=input('Password: '))",
               "show_products(conn,name=input('Search into list(for show all dont input any word!)'))",
               "insert_into_cart(conn,uproduct_name=input('Name of product u want to add:'),product_count=int(input('Number: ')))",
               "remove_from_cart(conn,name=input('What product u want to remove: '))",
               "show_cart(conn)",
               "submit(conn)",
               "exit()"
               ]
    num_options=[1,2,3,4,5,6,7,8]
    while True:
        print("\n1. LOGIN")
        print("2. SINGIN")
        print("3. SHOW LIST OF PRODUCTS")
        print("4. ADD ITEM TO CART")
        print("5. REMOVE ITEM FROM CART")
        print("6. SEE MY CART")
        print("7. FINISH ORDERING")
        print("8. CANCEL EVERY THINGS AND EXIT\n")
        option = zip(num_options,options)
        user_choose = int(input("SELECT YOUR CHOOSE: "))
        for munes, funcs in option:
            if user_choose == munes :
                eval(funcs)



def main():
    database = r"cart.sqlite"
    conn = create_connection(database)
    reset_table(conn)
    men_u()
main()

#YOUSOF.A.ASADI
#THANCKS REACH DOWN HEAR

#FUTURE UPDATES:
#1.ENCRYPTING PASSWORD
#2.AUTO GENERATE PASSWORD
#1.SALERS PANEL


