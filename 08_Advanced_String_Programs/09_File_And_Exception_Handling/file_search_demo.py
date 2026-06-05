file = open("sohan_master_profile.txt", "r")

data = file.read()

if "Python Programming" in data:
    print("Skill Found")
else:
    print("Skill Not Found")

file.close()