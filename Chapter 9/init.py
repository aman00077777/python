class Student :
    schoolName = "ABC School"

    def __init__(self, name):
        print("Whenever a new object is created I am called automatically")
        self.name = name
        print(self.name)

student1 = Student("Janvi")
print("Student 1",student1)

student2 = Student("Aman")