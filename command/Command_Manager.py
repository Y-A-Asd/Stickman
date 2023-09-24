from core.Actions import Damage, Money_Status, Army_Status, Add_Troops, Enemy_Status
from core.Troops.Miner import Miner
from core.Troops.Magikill import Magikill
from core.Troops.Giant import Giant
from core.Troops.Spearton import Spearton
from core.Troops.Archidon import Archidon
from core.Troops.Swordwarth import Swordwrath


def command_manager(req_list):
    for requests in req_list:
        command = requests[0]
        if command == "add":
            role, timestamp = requests[1].capitalize(), requests[2]
            result = Add_Troops.add_troop(eval(f"{role}"), timestamp)
        elif command == "damage":
            idx, d, timestamp = int(requests[1]), int(requests[2]), requests[3]
            result = Damage.damage(idx, d, timestamp)
        elif command == "enemy-status":
            timestamp = requests[1]
            result = Enemy_Status.enemy_status(timestamp)
        elif command == "army-status":
            timestamp = requests[1]
            result = Army_Status.army_status(timestamp)
        elif command == "money-status":
            timestamp = requests[1]
            result = Money_Status.money_status(timestamp)
        print(result)