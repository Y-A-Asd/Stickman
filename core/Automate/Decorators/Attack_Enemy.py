from core.Automate.Troops_Attack import attack
from core.Enemy import Enemy


def attack_enemy(func):
    def wrapper(*args):
        attack(args[-1])
        if Enemy.ORGINALHEALTH <= 0:
            return "game over"
        result = func(*args)
        return result

    return wrapper
