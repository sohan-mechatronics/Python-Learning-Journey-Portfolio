print("TABLES FROM 1 TO 10")

for table in range(1, 11):

    print("\nTable of", table)

    for num in range(1, 11):
        print(table, "x", num, "=", table * num)