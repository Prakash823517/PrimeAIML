# OOP -> mapping real world objects with code 

# class syntax

class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"

# object syntax

stu1 = Student() # object
# here object is created without _inin_Method
# bcz python automativally creates and execute it for us
stu2 = Student()
print(stu1) # it will give memory location of stu1

print(stu1.subject, stu1.college, stu1.year)
print(Student.subject)

print(type(stu1))

l = [1, 2]
s = set()
print(type(s))
print(type(l))
