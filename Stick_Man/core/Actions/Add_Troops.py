from Stick_Man.core.Automate.Timestamps import Timestaps
from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Player import Player
from Stick_Man.core.Automate.Decorators.Attack_Enemy import attack_enemy
from Stick_Man.core.Automate.Decorators.Check_Enemy import check_enemy
from Stick_Man.core.Automate.Decorators.Check_Money import check_money


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
