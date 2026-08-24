class Student:
    def __init__(self, name, cgpa): # constructor
        self.name = name # instance attribute(diff for all objects)
        self.cgpa = cgpa

    def get_cgpa(self): # instance method which has self parameter
        # self refers the object which is calling it 
        return self.cgpa

stu1 = Student("Rahul", 9.0)
stu2 = Student("Urvashi", 8.5)

print(stu1.get_cgpa()) # here self is stu1
