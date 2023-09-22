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
        #TODO :تکمیل بخش و گرفتن تست
        if Action.troops_capacity - type.unit < 0:
            return "Too many troops!"
        elif player.balance - type.cost < 0:
            return "Not enough money!"
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

enemy.health += 100
print(Action.income(3000))
print(Action.add_troop(eval("troops.giant")))
print(Action.add_troop(eval("troops.giant")))

print(Action.troops_capacity)
print(troops.Troops.troops)
print(Action.damage(1,100))
print(Action.income(200))
print(Action.attack(1))
"""
|====================================================================================================|
|                                              TASKs                                                 |
|====================================================================================================|
-Check enemy die every fucking time?
-Check max 50 units?
-Check max 8 miner?
-Organize code بهینه سازی کد
-Manage two inputs h&q h->enemy_health q->command_couter 
((function name))           describe                                    in%out                               
1.((attack))        troops can attack enemy             :Inputs->troops_id: :Output->status:                 
2.((kill_troop))    troops die if damage > health       :Inputs->troops_id: :Output->status:
3.((add_troop))     user can add troops                 :Inputs->troops_type: :Output->status:
4.((damage))        enemy damage us                     :Inputs->troops_id,damage_power: :Output->status:
5.((income))        every time calles should add income :Inputs->amount: :Output->status:
تمامی توابع مورد نیاز در سوال باید در پوشه action به صورت کامل باشد و استفاده آن در فایل main انجام میشود
در نظر بگیرید اگر در جایی از سوال خواستید ارور ریز کنید فقط توضیح آن را قابل فهم بگزارید و اگر در جایی از سوال 
احتمال بروز خطا در موارد خاص میدهید کامنت کنید تا در مرحله exeption handling فرد مربوطه بتواند بررسی کند
"""
