from core.Troops.Troops import Troops


class Miner(Troops):
    health = 100
    cost = 150
    speed = 10
    income = 100
    unit = 1

    def __init__(self, starttime):
        super().__init__(Miner.health, "miner", starttime)
