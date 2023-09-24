from Stick_Man.core.Automate.Timestamps import Timestaps
from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Automate.Attack import attack_enemy
from Stick_Man.core.Player import Player
from Stick_Man.core.Automate.Check_Enemy import check_enemy


@check_enemy
@attack_enemy
def add_troop(type, timestamps):  # type == one of trups class names
    if not issubclass(type, Troops):
        raise Exception()
    time_in_seconds = Timestaps(timestamps)
    if Player.balance - type.cost < 0:
        return "not enough money!"
    elif Troops.troops_capacity - type.unit < 0:
        return "too many troops!"
    else:
        Troops.troops_capacity -= type.unit
        Player.balance -= type.cost
        type(time=time_in_seconds)
        return Troops.troops_id
