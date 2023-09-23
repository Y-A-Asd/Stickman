from Stick_Man.core.Troops.Troops import Troops




def kill_troop(troops_id: int):
    if troops_id in Troops.troops:
        del Troops.troops[troops_id]
        return "done"
    else:
        return "Troop not exist"
