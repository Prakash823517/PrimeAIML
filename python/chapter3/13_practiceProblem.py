# Q) given a list of tuples with info(name, subject) :
    # list all unique course
    # list students enrolled in english 
    # create dictionary (student, set of courses)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

courses_set = set()
for tup in info:
    courses_set.add(tup[1])
print(courses_set)


# we can take different variable name for 
# iterable value 

courses_set2 = set()
# for name,course in info:
    # print(name, course);
    # courses_set2.add(course)
    # print(courses_set2)


for name, course in info:
    if (course == "English"):
        print(name)

# eng_students_set = set()
# for val in info:
#     if(val[1] == "English"):
#         eng_students_set.add(val[0])
    
# print(eng_students_set)


