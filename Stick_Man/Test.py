
from Stick_Man.core.Actions.Add_Troops import add_troop
from Stick_Man.core.Actions.Damage import damage
from Stick_Man.core.Actions.Army_Status import army_status
from Stick_Man.core.Actions.Enemy_Status import enemy_status
from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Actions.Money_Status import money_status
from Stick_Man.core.Troops.Miner import Miner
from Stick_Man.core.Troops.Giant import Giant





# print(Action.income(3000,"0:0:0"))
# Action.money_auto("0:0:00")
# print(player.balance)
print(add_troop(Miner,"0:0:000"))
# print(issubclass(Miner,Troops))
# print(Action.add_troop(eval("troops.miner"),"0:0:000"))
print(add_troop(Giant,"0:00:000"))
print(add_troop(Giant,"0:10:000"))
print(Troops.troops_capacity)
# print(Action.attack("00:20:000"))
# Action.money_auto("0:20:00")
# print(player.balance)
# print(Action.troops_capacity)
# print(troops.Troops.troops)
print(damage(1,90,"0:20:0"))
# print(damage(1,99,"0:21:0"))
# print(Action.income(200))
print(army_status("0:20:0"))
print(enemy_status("0:20:0"))
# print(Action.money_status("0:20:0"))
print(money_status("0:20:0"))
