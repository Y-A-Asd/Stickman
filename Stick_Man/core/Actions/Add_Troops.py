from Stick_Man.core.Automate.Timestamps import _timestamp
from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Automate.Attack import attack_enemy
from Stick_Man.core.Player import Player
from Stick_Man.core.Automate.Check_Enemy import check_enemy


@check_enemy
@attack_enemy
def add_troop(type, timestamps):  # type == one of trups class names
    time_in_seconds = _timestamp(timestamps)
    if Troops.troops_capacity - type.unit < 0:
        return "Too many troops!"
    elif Player.balance - type.cost < 0:
        return "Not enough money!"
    else:
        Troops.troops_capacity -= type.unit
        Player.balance -= type.cost
        type(time=time_in_seconds)
        return Troops.troops_id
