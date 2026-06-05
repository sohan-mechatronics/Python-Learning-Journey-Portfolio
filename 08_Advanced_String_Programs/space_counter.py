text = input("Enter Text: ")

count = 0

for ch in text:

    if ch == " ":
        count += 1

print("Spaces =", count)