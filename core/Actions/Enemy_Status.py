from core.Utils.Timestamps import Timestaps
from core.Enemy import Enemy
from core.Automate.Decorators.Attack_Enemy import attack_enemy
from core.Automate.Decorators.Check_Enemy import check_enemy
from core.Automate.Decorators.Check_Money import check_money


@check_money
@check_enemy
@attack_enemy
def enemy_status(timestamps):
    time_in_seconds = Timestaps(timestamps)
    return int(Enemy.ORGINALHEALTH)
