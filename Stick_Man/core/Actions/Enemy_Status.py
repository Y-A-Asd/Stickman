from Stick_Man.core.Automate.Timestamps import Timestaps
from Stick_Man.core.Enemy import Enemy
from Stick_Man.core.Automate.Attack import attack_enemy
from Stick_Man.core.Automate.Check_Enemy import check_enemy


@attack_enemy
@check_enemy
def enemy_status(timestamps):
    time_in_seconds = Timestaps(timestamps)
    return Enemy.remhealth
