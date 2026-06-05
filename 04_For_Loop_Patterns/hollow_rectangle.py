print("HOLLOW RECTANGLE")

for row in range(4):

    for col in range(6):

        if row == 0 or row == 3 or col == 0 or col == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()