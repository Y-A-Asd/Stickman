from core.Automate.Troops_Attack import attack


def attack_enemy(func):
    def wrapper(*args):
        attack(args[-1])
        result = func(*args)
        return result

    return wrapper
