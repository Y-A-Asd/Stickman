#HINT::::
from datetime import timedelta
time_input = input("Enter time in format mm,ss,fff: ")      # f -> milisecand
minute, second, millisecond = map(int, time_input.split(','))
time_difference = timedelta(seconds=4)
user_time = timedelta(minutes=minute, seconds=second, milliseconds=millisecond)
result_time = user_time + time_difference
result_formatted = f"{result_time.total_seconds() / 60:.0f},{result_time.seconds % 60:02},{result_time.microseconds // 1000:03}"
print(f"Original Time: {time_input}")
print(f"Time 4 Seconds Later: {result_formatted}")
#TODO