from core.Utils.Timestamps import Timestaps
from core.Troops.Troops import Troops
from core.Automate.Decorators.Attack_Enemy import attack_enemy




@attack_enemy
def army_status(timestamps):
    time_in_seconds = Timestaps(timestamps)
    troops_dict = {"giant": 0, "magikill": 0, "spearton": 0, "archidon": 0, "swordwrath": 0, "miner": 0}
    for i in list(Troops.troops.items()):
        if i[1].accessible:
            troop = i[1].type
            troops_dict[troop] += 1
    return " ".join(map(str, reversed(list(troops_dict.values()))))
