from Stick_Man.core.Enemy import Enemy


def check_enemy(func):
    def wrapper(*args):
        if Enemy.remhealth <= 0:
            exit("Dragon is dead")
        result = func(*args)
        return result

    return wrapper
