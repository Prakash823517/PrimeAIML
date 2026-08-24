class Student:
    subj = "Python"
    def __init__(self):
        # self value is passed automatically 
        print("constructor was called")

stu1 = Student()
#init method automatically call
print(stu1.subj)