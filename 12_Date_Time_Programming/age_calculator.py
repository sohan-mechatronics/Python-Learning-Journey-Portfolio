import datetime

birth_year = int(input("Enter Birth Year: "))

current_year = datetime.date.today().year

age = current_year - birth_year

print("Your Age =", age)