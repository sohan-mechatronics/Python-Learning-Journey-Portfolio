def sum_digits(num):

    total = 0

    while num > 0:

        digit = num % 10
        total = total + digit
        num = num // 10

    return total


number = int(input("Enter Number: "))

print("Sum of Digits =", sum_digits(number))