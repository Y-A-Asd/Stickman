from core.Troops.Troops import Troops


class Magikill(Troops):
    health = 80
    cost = 1200
    power = 200
    speed = 5
    unit = 4
    def __init__(self,starttime):
        super().__init__(Magikill.health, "magikill",starttime)
