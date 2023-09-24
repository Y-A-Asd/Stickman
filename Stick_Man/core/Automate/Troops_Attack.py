from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Enemy import Enemy
from Stick_Man.core.Automate.Timestamps import Timestaps
from Stick_Man.core.Automate.Cal_Timeingame import runtime


def attack(timestamps):
    time_in_seconds = Timestaps(timestamps)
    attack_damage: int = 0
    Enemy.NEWHEALTH = Enemy.ORGINALHEALTH
    for ids in Troops.troops:
        if Troops.troops[ids].type == "miner":  # if Troops.troops[ids].type != "miner":
            continue
        time_in_game = runtime(Troops.troops[ids].starttime,Troops.troops[ids].endtime,time_in_seconds)
        power = Troops.troops[ids].power
        speed = Troops.troops[ids].speed
        attack_damage += (time_in_game // speed) * power
    Enemy.NEWHEALTH -= attack_damage

