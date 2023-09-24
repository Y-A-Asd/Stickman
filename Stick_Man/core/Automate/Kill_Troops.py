from Stick_Man.core.Troops.Troops import Troops




def kill_troop(troops_id: int,time_in_seconds):
    if troops_id in Troops.troops:
        Troops.troops[troops_id].endtime = time_in_seconds
        return "done"
    else:
        return "Troop not exist"
