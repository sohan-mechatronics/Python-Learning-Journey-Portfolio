class Student:

    def __init__(self, name, branch, semester):

        self.name = name
        self.branch = branch
        self.semester = semester

    def show(self):

        print("Name =", self.name)
        print("Branch =", self.branch)
        print("Semester =", self.semester)
        print("-----------------")


s1 = Student("Sohan", "Mechatronics", 5)
s2 = Student("Rahul", "CSE", 3)
s3 = Student("Aman", "Electrical", 6)

s1.show()
s2.show()
s3.show()