from Stick_Man.core.Player import Player
from Stick_Man.core.Automate.Decorators.Attack_Enemy import attack_enemy
from Stick_Man.core.Automate.Decorators.Check_Enemy import check_enemy
from Stick_Man.core.Automate.Decorators.Check_Money import check_money


@check_money
@check_enemy
@attack_enemy
def money_status(timestamps):
    return Player.NEWBALANCE + Player.ORGINALBALANCE
