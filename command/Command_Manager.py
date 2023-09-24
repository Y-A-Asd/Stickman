from core.Actions import Damage, Money_Status, Army_Status, Add_Troops, Enemy_Status
from core.Troops.Miner import Miner
from core.Troops.Magikill import Magikill
from core.Troops.Giant import Giant
from core.Troops.Spearton import Spearton
from core.Troops.Archidon import Archidon
from core.Troops.Swordwarth import Swordwrath


class CommandManager:

    command_functions = {
        "add": Add_Troops.add_troop,
        "damage": Damage.damage,
        "enemy-status": Enemy_Status.enemy_status,
        "army-status": Army_Status.army_status,
        "money-status": Money_Status.money_status
    }
    @staticmethod
    def command_manager(req_list):
        for requests in req_list:
            command = requests[0]
            command_func = CommandManager.command_functions[command]
            args = requests[1:]
            result = command_func(*args)
            print(result)
