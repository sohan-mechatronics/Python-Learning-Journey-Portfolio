def largest(a, b):

    if a > b:
        return a

    else:
        return b

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Largest =", largest(num1, num2))