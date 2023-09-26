from core.Troops.Troops import Troops




def kill_troop(troops_id: int,time_in_seconds):
    Troops.troops[troops_id].endtime = time_in_seconds
    return "dead"

