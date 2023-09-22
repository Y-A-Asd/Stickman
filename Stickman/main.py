# #HINT::::
# from datetime import timedelta
# time_input = input("Enter time in format mm,ss,fff: ")      # f -> milisecand
# minute, second, millisecond = map(int, time_input.split(','))
# time_difference = timedelta(seconds=4)
# user_time = timedelta(minutes=minute, seconds=second, milliseconds=millisecond)
# result_time = user_time + time_difference
# result_formatted = f"{result_time.total_seconds() / 60:.0f},{result_time.seconds % 60:02},{result_time.microseconds // 1000:03}"
# print(f"Original Time: {time_input}")
# print(f"Time 4 Seconds Later: {result_formatted}")
# #TODO

from action import Action
import enemy
import player
def main():

    q, h = map(int, input().split()) #تو یک خط با فاصله
    enemy.health = h
    for _ in range(q):
        request = input().split()
        command = request[0]
        if command == "add":
            role, timestamp = request[1], request[2]
            result = Action.add_troop(role)
        elif command == "damage":
            idx, d, timestamp = int(request[1]), int(request[2]), request[3]
            result = Action.damage(idx, d)
        elif command == "enemy-status":
            timestamp = request[1]
            result = enemy.health
        elif command == "army-status":
            timestamp = request[1]
            result = Action.rmy_status()
        elif command == "money-status":
            timestamp = request[1]
            result = player.balance

        print(result)