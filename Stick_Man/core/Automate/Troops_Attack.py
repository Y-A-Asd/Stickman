from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Enemy import Enemy
from Stick_Man.core.Automate.Timestamps import _timestamp


def attack(timestamps):
    time_in_seconds = _timestamp(timestamps)
    attack_damage: int = 0
    for ids in Troops.troops:
        power = Troops.troops[ids].power
        speed = Troops.troops[ids].speed
        time = Troops.troops[ids].time
        attack_damage += ((time_in_seconds - time) // speed) * power
        # print(attack_damage)
    Enemy.remhealth -= attack_damage
    # print(Enemy.remhealth)
