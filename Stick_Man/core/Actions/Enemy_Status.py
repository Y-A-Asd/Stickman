from Stick_Man.core.Automate.Timestamps import Timestaps
from Stick_Man.core.Enemy import Enemy
from Stick_Man.core.Automate.Decorators.Attack_Enemy import attack_enemy
from Stick_Man.core.Automate.Decorators.Check_Enemy import check_enemy
from Stick_Man.core.Automate.Decorators.Check_Money import check_money


@check_money
@attack_enemy
@check_enemy
def enemy_status(timestamps):
    time_in_seconds = Timestaps(timestamps)
    return Enemy.NEWHEALTH
