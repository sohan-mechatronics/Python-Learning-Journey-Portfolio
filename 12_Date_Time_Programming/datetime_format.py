import datetime

current = datetime.datetime.now()

formatted = current.strftime("%d-%m-%Y %H:%M:%S")

print("Current Date & Time =", formatted)