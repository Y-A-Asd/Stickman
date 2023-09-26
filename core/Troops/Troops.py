from abc import ABC


class Troops(ABC):
    troops = dict()
    troops_id = 0
    troops_capacity = 50

    def __init__(self, health, type, starttime):
        Troops.troops_id += 1
        self.health = health
        self.type = type
        self.starttime = starttime
        self.accessible = True
        Troops.troops[Troops.troops_id] = self
