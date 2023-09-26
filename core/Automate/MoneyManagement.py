from core.Utils.Timestamps import Timestaps
from core.Troops.Troops import Troops
from core.Player import Player
from core.Utils.Cal_Timeingame import runtime


def income(num):
    Player.NEWBALANCE += num


def money_auto(timestamps):
    time_in_seconds = Timestaps(timestamps)
    amount = 0
    Player.NEWBALANCE = 0
    miner_counter = 0
    for ids in Troops.troops:
        if miner_counter < 8:
            if Troops.troops[ids].type == "miner":
                time_in_game = runtime(Troops.troops[ids].starttime, Troops.troops[ids].endtime, time_in_seconds)
                troop_income = Troops.troops[ids].income
                speed = Troops.troops[ids].speed
                amount += (time_in_game // speed) * troop_income
                miner_counter += 1
    amount += (time_in_seconds // 20) * 180
    income(amount)

