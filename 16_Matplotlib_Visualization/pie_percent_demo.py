import matplotlib.pyplot as plt

marks = [80, 70, 95]

students = ["Sohan", "Rahul", "Amit"]

plt.pie(
    marks,
    labels=students,
    autopct="%1.1f%%"
)

plt.title("Student Marks Distribution")

plt.show()