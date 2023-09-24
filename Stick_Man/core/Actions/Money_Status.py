from Stick_Man.core.Automate.MoneyManagement import money_auto
from Stick_Man.core.Player import Player
from Stick_Man.core.Automate.Decorators.Attack import attack_enemy
from Stick_Man.core.Automate.Decorators.Check_Enemy import check_enemy



@check_enemy
@attack_enemy
def money_status(timestamps):
    money_auto(timestamps)
    return Player.balance
