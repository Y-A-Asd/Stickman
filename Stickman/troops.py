# TODO: timer for each troop 
class Troops:
    troops = dict()
    troops_id = 0
    def __init__(self, health,type) :
        Troops.troops_id += 1
        self.health = health
        self.type = type
        Troops.troops[Troops.troops_id] = self
        
        
class miner(Troops):
    health = 100
    cost = 150
    power = 0
    speed = 10
    income = 100
    unit = 1
    def __init__(self):
        super().__init__(miner.health, "miner")
        self.active = True
    
        
class swordwrath(Troops):
    health = 120
    cost = 125
    power = 20
    speed = 1
    income = 0
    unit = 1
    def __init__(self):
        super().__init__(swordwrath.health, "swordwrath")
        
        
class archidon(Troops):
    health = 80
    cost = 300
    power = 10
    speed = 1
    income = 0
    unit = 1
    def __init__(self):
        super().__init__(archidon.health, "archidon")
        
class spearton(Troops):
    health = 250
    cost = 500
    power = 35
    speed = 3
    income = 0
    unit = 2
    def __init__(self):
        super().__init__(spearton.health, "spearton")
        
class magikill(Troops):
    health = 80
    cost = 1200
    power = 200
    speed = 5
    income = 0
    unit = 4
    def __init__(self):
        super().__init__(magikill.health, "magikill")
        
class giant(Troops):
    health = 1000 
    cost = 1500
    power = 150
    speed = 4
    income = 0
    unit = 4
    def __init__(self):        
        super().__init__(giant.health, "giant")
    
        
        

        
