# class Auth:
#     users = {}
#     def __init__(self):
#         pass
#     def add_user(self, user,passw):
#         if user not in self.__class__.users:
#             if len(passw) > 8:
#                 self.__class__.users[user] = passw
#             else:
#                 print("Password must be more than 8 characters")
#                 reise PasswordTooShort
#         else:
#             print("User already exists")
#             reise UserAlreadyExists
#     def login(self,user,passw):
#         if user in self.__class__.users:
#             if self.__class__.users[user] == passw:
#                 print("You are logged in")
#             else:
#                 print("Wrong password")
#                 reise WrongPassword
#
#         else:
#             print("User does not exist")
#             reise WrongUserName











import hashlib
import ts3_ex
import ts3_us


class Authenticator:
    def __init__(self):
        self.users = {}
    # ////////////////////////////////////////////////////////////////  کاربر جدید
    def add_user(self, username, password):
        if username in self.users:
            raise ts3_ex.UserAlreadyExists(username)
        if len(password) < 8:
            raise ts3_ex.PasswordTooShort(username)
        self.users[username] = ts3_us.User(username, password)
        print(f"user{username} signup!")
        return self.users[username]

    # ////////////////////////////////////////////////////////////////  ورود
    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise ts3_ex.WrongUserName(username)

        if user.password != hashlib.sha256(password.encode()).hexdigest():
            raise ts3_ex.WrongPassword(username)

        user.logged_in = True
        print(f"user{username} loging!")
        return True

    # ////////////////////////////////////////////////////////////////   چکینگ ورود
    def is_logged_in(self, username):
        return self.users[username].logged_in



add = Authenticator()
add.add_user("joun1","kfgdfu332dsf")
add.add_user("joun1","kfgdfufhsjf")
# add.add_user("joun2","kfg")
add.login("joun1","kfgdfu332dsf")
# add.login("joun1","kfgdfu2dsf")
# add.login("joun2","kfgdfu2dsf")
print(add.is_logged_in("joun1"))