import datetime

current_time = datetime.datetime.now()

clock = current_time.strftime("%H:%M:%S")

print("Current Time =", clock)