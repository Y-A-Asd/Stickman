from Stick_Man.core.Automate.MoneyManagement import money_auto


def check_money(func):
    def wrapper(*args):
        money_auto(args[-1])
        result = func(*args)
        return result

    return wrapper
