student_marks = {"Alice": 67, "prakash": 73, "Bob": 54, "Pop": 89}

key = input("press a key b/w 'A', 'B', 'C', 'D': ")

if(key == 'A'):
    name = input("enter name of student: ")
    marks = input("enter marks of student: ")
    student_marks[name] = marks
    print(student_marks)
elif(key == 'B'):
    for i in student_marks:
        student_marks[i] = int(input(f"{i} marks : "))
    print(student_marks)
elif(key == 'C'):
    name = input("enter the name of students: ")
    print(student_marks.get(name))
elif(key == 'D'):
    print(student_marks)
else:
    print("Invalid key")


