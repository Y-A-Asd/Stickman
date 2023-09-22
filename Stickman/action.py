import player
import troops
import enemy


class Action:
    troops_capacity = 50
    def attack(key:int):
        if enemy.health > 0:
            enemy.health -= troops.Troops.troops[key].power 
            if enemy.health <= 0:
               return "Dragon is dead"   
            return enemy.health
        else : return "Dragon is dead"

    def income(num:int):
        player.balance += num
        return player.balance
    def damage(key:int, power:int):
        troops.Troops.troops[key].health -= power
        if troops.Troops.troops[key].health <= 0:
            return Action.kill_troop(key)
        else:
            return troops.Troops.troops[key].health
    
    def add_troop(type): #type == one of trups class names
        
        if Action.troops_capacity - type.unit < 0:
            return "Too many troops!"
        elif player.balance - type.cost < 0:
            return "Not enough money!"
        else:
            Action.troops_capacity -= type.unit
            player.balance -= type.cost
            type()
            return troops.Troops.troops_id
        
    def kill_troop(key:int):
        if key in troops.Troops.troops:
            del troops.Troops.troops[key]
            return "done"
        else:
            return "Troop not exist"
enemy.health += 100
print(Action.income(3000))
print(Action.add_troop(eval("troops.giant")))
print(Action.add_troop(eval("troops.giant")))

print(Action.troops_capacity)
print(troops.Troops.troops)
print(Action.damage(1,100))
print(Action.income(200))
print(Action.attack(1))




    