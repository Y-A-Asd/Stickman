from Stick_Man.core.Troops.Troops import Troops


class Miner(Troops):
    health = 100
    cost = 150
    power = 0
    speed = 10
    income = 100
    unit = 1

    def __init__(self, time):
        super().__init__(Miner.health, "miner", time)