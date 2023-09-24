from Stick_Man.core.Automate.Troops_Attack import attack
from Stick_Man.core.Enemy import Enemy


def attack_enemy(func):
    def wrapper(*args):
        attack(args[-1])
        result = func(*args)
        return result

    return wrapper
