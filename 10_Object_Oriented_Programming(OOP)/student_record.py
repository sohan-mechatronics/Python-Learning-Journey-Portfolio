class Student:

    def __init__(self, name, branch, semester):

        self.name = name
        self.branch = branch
        self.semester = semester

    def show(self):

        print("Name =", self.name)
        print("Branch =", self.branch)
        print("Semester =", self.semester)


s1 = Student("Sohan", "Mechatronics", 5)

s1.show()