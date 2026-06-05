print("ATM PIN SYSTEM")

pin = "1234"

user_pin = input("Enter PIN: ")

while user_pin != pin:
    print("Invalid PIN")
    user_pin = input("Try Again: ")

print("Access Granted")
print("Welcome to ATM")