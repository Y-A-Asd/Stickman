from Stick_Man.core.Troops.Troops import Troops


class Giant(Troops):
    health = 1000
    cost = 1500
    power = 150
    speed = 4
    income = 0
    unit = 4
    def __init__(self,time):
        super().__init__(Giant.health, "giant",time)