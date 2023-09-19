class AuthException(Exception):
    pass
class UserAlreadyExists(AuthException):
    pass
class PasswordTooShort(AuthException):
    pass
class WrongUserName(AuthException):
    pass
class WrongPassword(AuthException):
    pass