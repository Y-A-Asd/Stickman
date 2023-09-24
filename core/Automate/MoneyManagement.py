from core.Automate.Timestamps import Timestaps
from core.Troops.Troops import Troops
from core.Player import Player
from core.Automate.Cal_Timeingame import runtime


def income(num):
    Player.NEWBALANCE += num


def money_auto(timestamps):
    time_in_seconds = Timestaps(timestamps)
    amount = 0
    Player.NEWBALANCE = 0
    for ids in Troops.troops:
        if Troops.troops[ids].type == "miner":
            time_in_game = runtime(Troops.troops[ids].starttime, Troops.troops[ids].endtime, time_in_seconds)
            troop_income = Troops.troops[ids].income
            speed = Troops.troops[ids].speed
            amount += (time_in_game // speed) * troop_income
    amount += (time_in_seconds // 20) * 180
    income(amount)

