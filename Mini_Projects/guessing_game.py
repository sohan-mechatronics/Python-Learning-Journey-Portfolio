print("GUESSING GAME")

secret = 7

guess = int(input("Guess Number: "))

while guess != secret:
    print("Wrong Guess")
    guess = int(input("Try Again: "))

print("Correct Guess")