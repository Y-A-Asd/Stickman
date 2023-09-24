from Stick_Man.core.Troops.Troops import Troops


class Spearton(Troops):
    health = 250
    cost = 500
    power = 35
    speed = 3
    income = 0
    unit = 2
    def __init__(self,starttime):
        super().__init__(Spearton.health, "spearton",starttime)