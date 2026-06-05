import math

print("1. Square Root")
print("2. Power")
print("3. Factorial")

choice = int(input("Enter Choice: "))

if choice == 1:

    num = int(input("Enter Number: "))
    print("Answer =", math.sqrt(num))

elif choice == 2:

    num = int(input("Enter Number: "))
    power = int(input("Enter Power: "))

    print("Answer =", math.pow(num, power))

elif choice == 3:

    num = int(input("Enter Number: "))
    print("Answer =", math.factorial(num))

else:

    print("Invalid Choice")