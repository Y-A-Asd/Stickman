from core.Utils.Timestamps import Timestaps
from core.Troops.Troops import Troops
from core.Player import Player
from core.Utils.Cal_Timeingame import runtime
from core.Troops.Game_based_money import GameBasedMoney
from core.Utils.Set_start_time import set_start_time


def income(num):
    Player.ORGINALBALANCE += num


def gamebasedmoney(time_in_second):
    delta_time = time_in_second - GameBasedMoney.starttime
    income = GameBasedMoney.income
    speed = GameBasedMoney.speed
    set_start_time(GameBasedMoney,runtime(GameBasedMoney,time_in_second))
    return delta_time // speed * income

def money_auto(timestamps):
    time_in_seconds = Timestaps(timestamps)
    amount = 0
    miner_counter = 0
    for ids in Troops.troops:
        if Troops.troops[ids].accessible:
            if miner_counter < 8:
                if Troops.troops[ids].type == "miner":
                    troop_income = Troops.troops[ids].income
                    speed = Troops.troops[ids].speed
                    delta_time = time_in_seconds-Troops.troops[ids].starttime
                    amount += delta_time//speed * troop_income
                    set_start_time(Troops.troops[ids], runtime(Troops.troops[ids], time_in_seconds))
                    miner_counter += 1
    amount += gamebasedmoney(time_in_seconds)
    income(amount)


