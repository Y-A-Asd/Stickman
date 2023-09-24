from core.Automate.Timestamps import Timestaps
from core.Troops.Troops import Troops
from core.Player import Player
from core.Automate.Decorators.Attack_Enemy import attack_enemy
from core.Automate.Decorators.Check_Enemy import check_enemy
from core.Automate.Decorators.Check_Money import check_money


@check_money
@check_enemy
@attack_enemy
def add_troop(type, timestamps):  # type == one of trups class names
    if not issubclass(type, Troops):
        raise Exception()
    time_in_seconds = Timestaps(timestamps)
    if Player.ORGINALBALANCE + Player.NEWBALANCE - type.cost < 0:
        return "not enough money!"
    elif Troops.troops_capacity - type.unit < 0:
        return "too many troops!"
    else:
        Troops.troops_capacity -= type.unit
        Player.ORGINALBALANCE -= type.cost
        type(starttime=time_in_seconds)
        return Troops.troops_id
