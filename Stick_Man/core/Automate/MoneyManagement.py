from Stick_Man.core.Automate.Timestamps import Timestaps
from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Player import Player



def income(num):
    Player.balance += num


def money_auto(timestamps):
    time_in_seconds = Timestaps(timestamps)
    amount = 0
    for ids in Troops.troops:
        if Troops.troops[ids].type == "miner":
            troop_income = Troops.troops[ids].income
            speed = Troops.troops[ids].speed
            time = Troops.troops[ids].time
            amount += ((time_in_seconds - time) // speed) * troop_income
    amount += (time_in_seconds // 20) * 180
    income(amount)

