from core.Troops.Troops import Troops


class Archidon(Troops):
    health = 80
    cost = 300
    power = 10
    speed = 1
    unit = 1
    def __init__(self,starttime):
        super().__init__(Archidon.health, "archidon",starttime)
