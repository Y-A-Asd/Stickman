from core.Utils.Timestamps import Timestaps
from core.Troops.Troops import Troops
from core.Player import Player
from core.Automate.Decorators.Attack_Enemy import attack_enemy
from core.Automate.Decorators.Check_Enemy import check_enemy
from core.Automate.Decorators.Check_Money import check_money
from core.Troops.Miner import Miner
from core.Troops.Magikill import Magikill
from core.Troops.Giant import Giant
from core.Troops.Spearton import Spearton
from core.Troops.Archidon import Archidon
from core.Troops.Swordwarth import Swordwrath

@check_money
@check_enemy
@attack_enemy
def add_troop(troops_type: str, timestamps):  # type == one of trups class names
    troops_type = eval(troops_type.capitalize())
    time_in_seconds = Timestaps(timestamps)
    if Player.ORGINALBALANCE - troops_type.cost < 0:
        return "not enough money!"
    elif Troops.troops_capacity - troops_type.unit < 0:
        return "too many troops!"
    else:
        Troops.troops_capacity -= troops_type.unit
        Player.ORGINALBALANCE -= troops_type.cost
        troops_type(starttime=time_in_seconds)
        return Troops.troops_id
