import matplotlib.pyplot as plt

students = ["Sohan", "Rahul", "Amit"]

marks = [80, 70, 90]

plt.bar(students, marks)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()