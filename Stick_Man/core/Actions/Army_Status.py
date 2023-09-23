from Stick_Man.core.Automate.Timestamps import _timestamp
from Stick_Man.core.Troops.Troops import Troops
from Stick_Man.core.Automate.Attack import attack_enemy
from Stick_Man.core.Automate.Check_Enemy import check_enemy


@attack_enemy
@check_enemy
def army_status(timestamps):
    time_in_seconds = _timestamp(timestamps)
    troops_dict = {"giant": 0, "magikill": 0, "spearton": 0, "archidon": 0, "swordwrath": 0, "miner": 0}
    for i in list(Troops.troops.items()):
        troop = i[1].type
        troops_dict[troop] += 1
    return " ".join(map(str, reversed(list(troops_dict.values()))))