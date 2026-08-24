# list -> mutable sequence of values

marks = [99, 89, 100, 65, 92, 95.92, "abc", "python"]
print(marks)
print(marks[1])
print(len(marks))

marks[2] = 70
print(marks)
print(type(marks))

# list slicing 
print(marks[0:5])
print(marks[5: len(marks)])
print(marks[-5: -2])