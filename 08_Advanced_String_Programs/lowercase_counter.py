text = input("Enter Text: ")

count = 0

for ch in text:

    if ch.islower():
        count += 1

print("Lowercase Letters =", count)