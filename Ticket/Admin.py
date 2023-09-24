from Users import Users

def admin():
    pass

class Admin(Users):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.status = Admin.check(self)

    def check(self):
        if self.password == "admin" and self.username == "admin":
            return True
        else:
            return False
