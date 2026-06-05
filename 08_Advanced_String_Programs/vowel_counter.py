text = input("Enter Text: ")

count = 0

for ch in text:

    if ch in "AEIOUaeiou":
        count += 1

print("Total Vowels =", count)