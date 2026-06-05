print("STRING MASTER DEMO")

name = "SOHAN"

print("\nOriginal String =", name)

# Length
print("Length =", len(name))

# Positive Indexing
print("First Character =", name[0])
print("Second Character =", name[1])

# Negative Indexing
print("Last Character =", name[-1])
print("Second Last =", name[-2])

# Slicing
print("0 to 3 =", name[0:3])
print("1 to 4 =", name[1:4])

# Reverse String
print("Reverse =", name[::-1])

# Upper & Lower
print("Upper =", name.upper())
print("Lower =", name.lower())

# Replace
print("Replace S with M =", name.replace("S", "M"))

# Count
print("Count of A =", name.count("A"))

# Find
print("Index of H =", name.find("H"))