print("=== SIMPLE CALCULATOR ===")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation: +  -  *  /")
op = input("Enter operator: ")

if op == "+":
    print("Answer =", a + b)

elif op == "-":
    print("Answer =", a - b)

elif op == "*":
    print("Answer =", a * b)

elif op == "/":
    print("Answer =", a / b)

else:
    print("Invalid operator")

    