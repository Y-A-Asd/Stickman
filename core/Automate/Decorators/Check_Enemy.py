from core.Enemy import Enemy


def check_enemy(func):
    def wrapper(*args):
        if Enemy.ORGINALHEALTH <= 0:
            exit("Dragon is dead")
        result = func(*args)
        return result
    return wrapper
