text = input("Enter Text: ")

count = 0

for ch in text:

    if ch.isupper():
        count += 1

print("Uppercase Letters =", count)