class Student:
    college_name = "ABC college" # class attribute
    PI = 3.1

    def __init__(self, name, gpa):
        self.name = name # instance attribute
        self.gpa = gpa
        self.PI = 3.14

stu1 = Student("Rahul", 9.2)

# instance attribute can not be accessed throgh class name 
# print(Student.name) 

# instance attribut can only be accessed through object name
print(stu1.name)

# class attribute can be accessed by both class name and object name 
print(stu1.college_name)
print(Student.college_name)

# instance attribut has higher priority
print(stu1.PI) # it will give instance attribute
print(Student.PI) # it will give class attribute