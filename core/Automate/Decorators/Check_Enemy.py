from core.Utils.Enemy import Enemy


def check_enemy(func):
    def wrapper(*args):
        if Enemy.NEWHEALTH <= 0:
            return "Dragon is dead"
        result = func(*args)
        return result
    return wrapper
