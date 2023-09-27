from core.Utils.Timestamps import Timestaps
from core.Enemy import Enemy
from core.Automate.Decorators.Attack_Enemy import attack_enemy





@attack_enemy
def enemy_status(timestamps):
    time_in_seconds = Timestaps(timestamps)
    return int(Enemy.ORGINALHEALTH)
