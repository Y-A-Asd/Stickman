from abc import ABC


class Troops(ABC):
    troops = dict()
    troops_id = 0
    troops_capacity = 50

    def __init__(self, health, type, time):
        Troops.troops_id += 1
        self.health = health
        self.type = type
        self.time = time
        Troops.troops[Troops.troops_id] = self
