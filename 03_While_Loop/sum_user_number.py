print("SUM UP TO USER NUMBER")

num = int(input("Enter Number: "))

count = 1
total = 0

while count <= num:
    total = total + count
    count = count + 1

print("Total =", total)