from core.Player import Player
from core.Automate.Decorators.Attack_Enemy import attack_enemy
from core.Automate.Decorators.Check_Enemy import check_enemy
from core.Automate.Decorators.Check_Money import check_money


@check_money
@check_enemy
@attack_enemy
def money_status(timestamps):
    return int(Player.ORGINALBALANCE)
