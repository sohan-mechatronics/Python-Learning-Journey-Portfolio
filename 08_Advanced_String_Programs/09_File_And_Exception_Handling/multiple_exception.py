try:
    num = int(input("Enter Number: "))

    result = 100 / num

    print("Result =", result)

except ValueError:
    print("Please Enter Numbers Only")

except ZeroDivisionError:
    print("Cannot Divide By Zero")