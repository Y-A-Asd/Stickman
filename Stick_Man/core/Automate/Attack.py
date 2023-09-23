from Stick_Man.core.Automate.Troops_Attack import attack
from Stick_Man.core.Enemy import Enemy


def attack_enemy(func):
    def wrapper(*args):
        Enemy.remhealth = Enemy.fhealth
        attack(args[-1])
        result = func(*args)
        return result

    return wrapper
