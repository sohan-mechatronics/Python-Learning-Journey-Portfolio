print("PASSWORD SYSTEM")

password = "python123"

user = input("Enter Password: ")

while user != password:
    print("Wrong Password")
    user = input("Try Again: ")

print("Access Granted")