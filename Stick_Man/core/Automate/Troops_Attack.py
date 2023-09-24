from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Enemy import Enemy
from Stick_Man.core.Automate.Timestamps import Timestaps


def attack(timestamps):
    time_in_seconds = Timestaps(timestamps)
    attack_damage: int = 0
    for ids in Troops.troops:
        power = Troops.troops[ids].power
        speed = Troops.troops[ids].speed
        time = Troops.troops[ids].starttime
        attack_damage += ((time_in_seconds - time) // speed) * power
    Enemy.remhealth -= attack_damage
    # print(Enemy.remhealth)
