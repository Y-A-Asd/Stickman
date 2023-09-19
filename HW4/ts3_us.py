import hashlib
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.logged_in = False