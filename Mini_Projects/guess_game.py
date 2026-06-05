import random

print("🎯 === GUESS THE NUMBER GAME ===")

secret = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < secret:
        print("📉 Too Low! Try again")

    elif guess > secret:
        print("📈 Too High! Try again")

    else:
        print("🎉 Correct Guess!")
        print("Attempts taken:", attempts)
        break

print("Game Over 👋")