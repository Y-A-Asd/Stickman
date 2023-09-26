from core.Troops.Troops import Troops
from core.Utils.Enemy import Enemy
from core.Utils.Timestamps import Timestaps
from core.Utils.Cal_Timeingame import runtime


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

