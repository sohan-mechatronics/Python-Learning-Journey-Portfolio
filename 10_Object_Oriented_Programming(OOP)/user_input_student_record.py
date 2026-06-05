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


name = input("Enter Name: ")
branch = input("Enter Branch: ")
semester = int(input("Enter Semester: "))

s1 = Student(name, branch, semester)

s1.show()