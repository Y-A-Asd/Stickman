import player
import troops
import enemy


class Action:
    troops_capacity = 50

    def attack(troops_id:int):
        if enemy.health > 0:
            enemy.health -= troops.Troops.troops[troops_id].power
            if enemy.health <= 0:
               return "Dragon is dead"   
            return enemy.health
        else : return "Dragon is dead"

    def income(num:int):
        player.balance += num
        return player.balance
    def damage(troops_id:int, power:int):
        troops.Troops.troops[troops_id].health -= power
        if troops.Troops.troops[troops_id].health <= 0:
            return Action.kill_troop(troops_id)
        else:
            return troops.Troops.troops[troops_id].health
    
    def add_troop(type): #type == one of trups class names
        if Action.troops_capacity - type.unit < 0:
            return "Too many troops!"
        elif player.balance - type.cost < 0:
            return "Not enough money!"
        else:
            if isinstance(type, troops.miner):
                if Action.find_miners():
                    Action.troops_capacity -= type.unit
                    player.balance -= type.cost
                    type()
                else:
                    Action.troops_capacity -= type.unit
                    player.balance -= type.cost
                    type()
                    type.active = False
            else:
                Action.troops_capacity -= type.unit
                player.balance -= type.cost
                type()
            return troops.Troops.troops_id
        
    def kill_troop(troops_id:int):
        if troops_id in troops.Troops.troops:
            del troops.Troops.troops[troops_id]
            return "done"
        else:
            return "Troop not exist"
    @staticmethod
    def army_status():
        troopsi = {"giant": 0, "magikill": 0, "spearton": 0, "archidon": 0, "swordwrath": 0, "miner": 0}
        for i in list(troops.Troops.troops.items()):
            troop = i[1].type
            troopsi[troop] += 1
        print(" ".join(map(str, troopsi.values())))
        print(" ".join(map(str, reversed(list(troopsi.values())))))
    @staticmethod
    def find_miners():
        return sum(1 for troop in troops.Troops.troops.values() if troop.type == "miner") <= 8
            # sum = 0
            # for i in list(troops.Troops.troops.items()):
            #     troop = i[1].type
            #     if troop == "miner":
            #         sum += 1
            # if sum > 8:
            #     return False
            # else:
            #     return True



enemy.health += 100
print(Action.income(3000))
print(Action.add_troop(eval("troops.giant")))
print(Action.add_troop(eval("troops.giant")))

print(Action.troops_capacity)
print(troops.Troops.troops)
print(Action.damage(1,100))
print(Action.income(200))
print(Action.attack(1))
Action.army_status()
"""

|================================================================================================================|
|                                                      TASKs                                                     |
|================================================================================================================|
  -Check max 50 units?                                                                                           |
  -Check max 8 miner?                                                                                            |
  -Check enemy die every fucking time?                                                                           |
  -Organize code بهینه سازی کد organize player and enemy files :/                                                |
  -Manage two inputs h&q h->enemy_health q->command_couter 
  
  ((function name))           describe                                  in & out                               
  1.((attack))        troops can attack enemy             :Inputs->troops_id:               :Output->status:                 
  2.((kill_troop))    troops die if damage > health       :Inputs->troops_id:               :Output->status:
  3.((add_troop))     user can add troops                 :Inputs->troops_type:             :Output->status:
  4.((damage))        enemy damage us                     :Inputs->troops_id,damage_power:  :Output->status:
  5.((income))        every time calles should add income :Inputs->amount:                  :Output->status:
  6.((army_status))   show status of army as question ask                                   :Output->status:
  
  تمامی توابع مورد نیاز در سوال باید در پوشه action به صورت کامل باشد و استفاده آن در فایل main انجام میشود
  در نظر بگیرید اگر در جایی از سوال خواستید ارور ریز کنید فقط توضیح آن را قابل فهم بگزارید و اگر در جایی از سوال
  احتمال بروز خطا در موارد خاص میدهید کامنت کنید تا در مرحله exeption handling فرد مربوطه بتواند بررسی کند
  
"""
