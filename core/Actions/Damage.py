from core.Automate.Timestamps import Timestaps
from core.Troops.Troops import Troops
from core.Automate.Decorators.Attack_Enemy import attack_enemy
from core.Automate.Kill_Troops import kill_troop
from core.Automate.Decorators.Check_Enemy import check_enemy
from core.Automate.Decorators.Check_Money import check_money


@check_money
@check_enemy
@attack_enemy
def damage(troops_id: int, power: int, timestamps):
    time_in_seconds = Timestaps(timestamps)
    try:
        if Troops.troops[troops_id].endtime:
            raise Exception()
        Troops.troops[troops_id].health -= power
    except:
        return "no matter"
    if Troops.troops[troops_id].health <= 0:
        return kill_troop(troops_id,time_in_seconds)
    else:
        return Troops.troops[troops_id].health
