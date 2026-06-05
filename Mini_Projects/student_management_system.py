class Student:

    def __init__(self, name, branch, semester):

        self.name = name
        self.branch = branch
        self.semester = semester

    def show(self):

        print("\nStudent Details")
        print("Name =", self.name)
        print("Branch =", self.branch)
        print("Semester =", self.semester)


student_list = []

for i in range(3):

    print("\nEnter Student", i + 1)

    name = input("Name: ")
    branch = input("Branch: ")
    semester = int(input("Semester: "))

    student = Student(name, branch, semester)

    student_list.append(student)


print("\n===== ALL STUDENTS =====")

for student in student_list:

    student.show()