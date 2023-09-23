from Stick_Man.core.Automate.Timestamps import _timestamp
from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Automate.Attack import attack_enemy
from Stick_Man.core.Automate.Kill_Troops import kill_troop
from Stick_Man.core.Automate.Check_Enemy import check_enemy


@check_enemy
@attack_enemy
def damage(troops_id: int, power: int, timestamps):
    time_in_seconds = _timestamp(timestamps)
    Troops.troops[troops_id].health -= power
    if Troops.troops[troops_id].health <= 0:
        return kill_troop(troops_id)
    else:
        return Troops.troops[troops_id].health
