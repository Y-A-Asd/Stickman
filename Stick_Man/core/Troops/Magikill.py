from Stick_Man.core.Troops.Troops import Troops


class Magikill(Troops):
    health = 80
    cost = 1200
    power = 200
    speed = 5
    income = 0
    unit = 4
    def __init__(self,starttime):
        super().__init__(Magikill.health, "magikill",starttime)