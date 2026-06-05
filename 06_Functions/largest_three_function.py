def largest(a, b, c):

    if a > b and a > c:
        return a

    elif b > c:
        return b

    else:
        return c


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

print("Largest Number =", largest(num1, num2, num3))