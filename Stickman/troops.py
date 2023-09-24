from abc import ABC


class Troops(ABC):
    troops = dict()
    troops_id = 0
    
    def __init__(self, health,type,time) :
        Troops.troops_id += 1
        self.health = health
        self.type = type
        self.time = time
        Troops.troops[Troops.troops_id] = self
        
        
class Miner(Troops):
    health = 100
    cost = 150
    power = 0
    speed = 10
    income = 100
    unit = 1
    def __init__(self,time):
        super().__init__(Miner.health, "miner",time)
    
        
class Swordwrath(Troops):
    health = 120
    cost = 125
    power = 20
    speed = 1
    income = 0
    unit = 1
    def __init__(self,time):
        super().__init__(Swordwrath.health, "swordwrath",time)
        
        
class Archidon(Troops):
    health = 80
    cost = 300
    power = 10
    speed = 1
    unit = 1
    def __init__(self,time):
        super().__init__(Archidon.health, "archidon",time)
        
class Spearton(Troops):
    health = 250
    cost = 500
    power = 35
    speed = 3
    income = 0
    unit = 2
    def __init__(self,time):
        super().__init__(Spearton.health, "spearton",time)
        
class Magikill(Troops):
    health = 80
    cost = 1200
    power = 200
    speed = 5
    income = 0
    unit = 4
    def __init__(self,time):
        super().__init__(Magikill.health, "magikill",time)
        
class Giant(Troops):
    health = 1000 
    cost = 1500
    power = 150
    speed = 4
    income = 0
    unit = 4
    def __init__(self,time):
        super().__init__(Giant.health, "giant",time)
    
        
        

        
