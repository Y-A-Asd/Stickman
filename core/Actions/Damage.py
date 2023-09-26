from core.Automate.Decorators.Attack_Enemy import attack_enemy
from core.Automate.Decorators.Check_Enemy import check_enemy
from core.Automate.Decorators.Check_Money import check_money
from core.Utils.Kill_Troops import kill_troop
from core.Utils.Timestamps import Timestaps
from core.Troops.Troops import Troops


@check_money
@check_enemy
@attack_enemy
def damage(troops_id: int, power: int, timestamps):
    time_in_seconds = Timestaps(timestamps)
    troops_id = int(troops_id)
    power = int(power)
    try:
        if not Troops.troops[troops_id].accessible:
            raise Exception()
        Troops.troops[troops_id].health -= power
    except:
        return "no matter"
    if Troops.troops[troops_id].health <= 0:
        return kill_troop(troops_id, time_in_seconds)
    else:
        return Troops.troops[troops_id].health
