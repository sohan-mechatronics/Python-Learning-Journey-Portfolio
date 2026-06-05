print("SUM UP TO USER NUMBER")

num = int(input("Enter Number: "))

total = 0

for count in range(1, num + 1):
    total = total + count

print("Total =", total)