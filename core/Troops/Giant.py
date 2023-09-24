from core.Troops.Troops import Troops


class Giant(Troops):
    health = 1000
    cost = 1500
    power = 150
    speed = 4
    unit = 4
    def __init__(self,starttime):
        super().__init__(Giant.health, "giant",starttime)