file = open("sohan_master_profile.txt", "w")

file.write("========== SOHAN MASTER PROFILE ==========\n\n")

file.write("PERSONAL DETAILS\n")
file.write("Name : Sohan Kumar\n")
file.write("City : Katihar\n\n")

file.write("DIPLOMA EDUCATION\n")
file.write("Branch : Electrical Engineering\n")
file.write("Qualification : Diploma\n\n")

file.write("B.E. EDUCATION\n")
file.write("Branch : Mechatronics Engineering\n")
file.write("College : Chandigarh University\n")
file.write("Location : Gharuan, Mohali\n")
file.write("Status : Pursuing\n\n")

file.write("SKILLS\n")
file.write("Python Programming\n")
file.write("PLC\n")
file.write("HMI\n")
file.write("Industrial Automation\n")
file.write("Robotics\n\n")

file.write("PROJECTS\n")
file.write("Python Programs Collection\n")
file.write("Student Management System\n\n")

file.close()

print("Profile Saved Successfully")