from Stick_Man.core.Troops.Troops import Troops


class Archidon(Troops):
    health = 80
    cost = 300
    power = 10
    speed = 1
    income = 0
    unit = 1
    def __init__(self,time):
        super().__init__(Archidon.health, "archidon",time)