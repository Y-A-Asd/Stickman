from core.Troops.Troops import Troops
from core.Enemy import Enemy
from core.Utils.Timestamps import Timestaps
from core.Utils.Cal_Timeingame import runtime
from core.Utils.Set_start_time import set_start_time


def attack(timestamps):
    time_in_seconds = Timestaps(timestamps)
    attack_damage: int = 0
    for ids in Troops.troops:
        if Troops.troops[ids].accessible:
            if Troops.troops[ids].type == "miner":  # if Troops.troops[ids].type != "miner":
                continue
            power = Troops.troops[ids].power
            speed = Troops.troops[ids].speed
            delta_time = time_in_seconds-Troops.troops[ids].starttime
            attack_damage += delta_time // speed * power
            set_start_time(Troops.troops[ids], runtime(Troops.troops[ids], time_in_seconds))
    Enemy.ORGINALHEALTH -= attack_damage

