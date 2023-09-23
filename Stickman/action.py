import player
import troops
import enemy


class Action:
    troops_capacity = 50


#TODO:Decorator
    @staticmethod
    def mydec(func):
        def wrapper(*args):
            Action.attack(args[-1])
            result = func(args)
            return result
        return wrapper()

    def _timestamp(timestamps):
        minutes, seconds, milliseconds = map(int, timestamps.split(':'))
        time_in_seconds = minutes * 60 + seconds + milliseconds / 1000
        return time_in_seconds
    @staticmethod
    def attack(timestamps):
        time_in_seconds = Action._timestamp(timestamps)
        attack = 0
        for ids in troops.Troops.troops:
            power = troops.Troops.troops[ids].power
            speed = troops.Troops.troops[ids].speed
            time = troops.Troops.troops[ids].time
            attack += ((time_in_seconds - time) // speed) * power
        enemy.health -= attack




    @staticmethod
    def money_auto(timestamps):
        time_in_seconds = Action._timestamp(timestamps)
        amount = 0
        for ids in troops.Troops.troops:
            if troops.Troops.troops[ids].type == "miner":
                income = troops.Troops.troops[ids].income
                speed = troops.Troops.troops[ids].speed
                time = troops.Troops.troops[ids].time
                amount += ((time_in_seconds - time) // speed) * income
        amount += (time_in_seconds//20) * 180
        Action.income(amount)



    @staticmethod
    def income(num):
        player.balance += num


    @classmethod
    def money_status(cls,timestamps):
        cls.money_auto(timestamps)
        return player.balance

    @staticmethod
    def damage(troops_id:int, power:int,timestamps):
        time_in_seconds = Action._timestamp(timestamps)

        troops.Troops.troops[troops_id].health -= power
        if troops.Troops.troops[troops_id].health <= 0:
            return Action.kill_troop(troops_id)
        else:
            return troops.Troops.troops[troops_id].health

    def add_troop(type,timestamps): #type == one of trups class names
        time_in_seconds = Action._timestamp(timestamps)
        if Action.troops_capacity - type.unit < 0:
            return "Too many troops!"
        elif player.balance - type.cost < 0:
            return "Not enough money!"
        else:
            Action.troops_capacity -= type.unit
            player.balance -= type.cost
            type(time=time_in_seconds)
            return troops.Troops.troops_id




    def kill_troop(troops_id:int):
        if troops_id in troops.Troops.troops:
            del troops.Troops.troops[troops_id]
            return "done"
        else:
            return "Troop not exist"

    @mydec
    @staticmethod
    def enemy_status(timestamps):
        Action.attack(timestamps)
        if enemy.health <= 0:
            exit("Dragon is dead")
        else:
            return enemy.health



    @staticmethod
    def army_status():
        # time_in_seconds = Action._timestamp(timestamps)
        troopsi = {"giant": 0, "magikill": 0, "spearton": 0, "archidon": 0, "swordwrath": 0, "miner": 0}
        # print(list(troops.Troops.troops.items()))
        for i in list(troops.Troops.troops.items()):
            troop = i[1].type
            troopsi[troop] += 1
        # print(" ".join(map(str, troopsi.values())))
        print(" ".join(map(str, reversed(list(troopsi.values())))))



            # sum = 0
            # for i in list(troops.Troops.troops.items()):
            #     troop = i[1].type
            #     if troop == "miner":
            #         sum += 1
            # if sum > 8:
            #     return False
            # else:
            #     return True



enemy.health += 150
# print(Action.income(3000,"0:0:0"))
# Action.money_auto("0:0:00")
# print(player.balance)
print(Action.add_troop(eval("troops.miner"),"0:0:000"))
# print(Action.add_troop(eval("troops.miner"),"0:0:000"))
# print(player.balance)
print(Action.add_troop(eval("troops.giant"),"0:00:000"))
print(Action.add_troop(eval("troops.giant"),"0:10:000"))
# print(Action.attack("00:20:000"))
# Action.money_auto("0:20:00")
# print(player.balance)
# print(Action.troops_capacity)
# print(troops.Troops.troops)
# print(Action.damage(1,100))
# print(Action.income(200))
Action.army_status("0:10:0")
print(Action.enemy_status("0:20:0"))
# print(Action.money_status("0:20:0"))

"""

|================================================================================================================|
|                                                      TASKs                                                     |
|================================================================================================================|
  -Check max 50 units?                                                                                           |
  -Check max 8 miner?                                                                                            |
  -Check enemy die every fucking time?                                                                           |
  -Organize code بهینه سازی کد organize player and enemy files :/                                                |
  -Manage two inputs h&q h->enemy_health q->command_couter 
  
  ((function name))           describe                                      in & out
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
