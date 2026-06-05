import matplotlib.pyplot as plt

marks = [80, 70, 95]

students = ["Sohan", "Rahul", "Amit"]

explode = [0, 0, 0.2]

plt.pie(
    marks,
    labels=students,
    autopct="%1.1f%%",
    explode=explode
)

plt.title("Student Marks Distribution")

plt.savefig("student_marks.png")

plt.show()