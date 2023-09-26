from core.Troops.Troops import Troops


def runtime(troop: Troops, time_in_seconds):
    I = troop.starttime
    while I < time_in_seconds:
        I += troop.speed
    return round(I - troop.speed)
